"""Leetcode 981. Time Based Key-Value Store
Medium

URL: https://leetcode.com/problems/time-based-key-value-store/

Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)
- Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)
- Returns a value such that set(key, value, timestamp_prev) was called previously,
  with timestamp_prev <= timestamp.
- If there are multiple such values, it returns the one with the largest timestamp_prev.
- If there are no values, it returns the empty string ("").

Example 1:
Input: inputs = ["TimeMap","set","get","get","set","get","get"], 
inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:   
TimeMap kv;   
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1   
kv.get("foo", 1); // output "bar"   
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at 
                  // timestamp 3 and timestamp 2, then the only value is at timestamp
                  // 1 ie "bar"   
kv.set("foo", "bar2", 4);   
kv.get("foo", 4); // output "bar2"   
kv.get("foo", 5); // output "bar2"   

Example 2:
Input: inputs = ["TimeMap","set","set","get","get","get","get","get"],
inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],
          ["love",20],["love",25]]
Output: [null,null,null,"","high","high","low","low"]

Note:
- All key/value strings are lowercase.
- All key/value strings have length in the range [1, 100]
- The timestamps for all TimeMap.set operations are strictly increasing.
- 1 <= timestamp <= 10^7
- TimeMap.set and TimeMap.get functions will be called a total of 120000 times 
  (combined) per test case.
"""

class TimeMapBinarySearchGet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Use key_timestampvalues dict: key->[timestamp, value].
        from collections import defaultdict

        self.key_timestampvalues = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None

        Time complexity: O(1).
        Space complexity: O(n), where n is the number of stored key-values.
        """
        self.key_timestampvalues[key].append([timestamp, value])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str

        Time complexity: O(logn), where n is the number of stored key-values.
        Space complexity: O(n).
        """
        # Since timestamp are sorted, use Binary Search to get value.

        # Edge case.
        if key not in self.key_timestampvalues:
            return ''

        timestamp_values = self.key_timestampvalues[key]

        left, right = 0, len(timestamp_values) - 1
        while left < right:
            mid = left + (right - left) // 2

            if timestamp_values[mid][0] == timestamp:
                return timestamp_values[mid][1]
            elif timestamp_values[mid][0] < timestamp:
                # Check if moving left to feasible range.
                if timestamp_values[mid + 1][0] > timestamp:
                    return timestamp_values[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        # For left = right, check if there is reasonable timestamp.
        if timestamp_values[left][0] <= timestamp:
            return timestamp_values[left][1]
        else:
            return ''


def main():
    timemap = TimeMapBinarySearchGet()
    timemap.set("foo", "bar", 1)
    print timemap.get("foo", 1)  # Output: 'bar'
    print timemap.get("foo", 3)  # Output: 'bar'
    timemap.set("foo", "bar2", 4)
    print timemap.get("foo", 4)  # Output: 'bar2'
    print timemap.get("foo", 5)  # Output: 'bar2'

    timemap = TimeMapBinarySearchGet()
    timemap.set("love", "high", 10)
    timemap.set("love", "low", 20)
    print timemap.get("love", 5)   # Output: ''
    print timemap.get("love", 10)  # Output: 'high'
    print timemap.get("love", 15)  # Output: 'high'
    print timemap.get("love", 20)  # Output: 'low'
    print timemap.get("love", 25)  # Output: 'low'


if __name__ == '__main__':
    main()
