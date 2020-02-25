"""Leetcode 1024. Video Stitching
Medium

URL: https://leetcode.com/problems/video-stitching/

You are given a series of video clips from a sporting event that lasted
T seconds.  These video clips can be overlapping with each other and
have varied lengths.

Each video clip clips[i] is an interval: it starts at time clips[i][0]
and ends at time clips[i][1].  We can cut these clips into segments
freely: for example, a clip [0, 7] can be cut into segments
[0, 1] + [1, 3] + [3, 7].

Return the minimum number of clips needed so that we can cut the clips
into segments that cover the entire sporting event ([0, T]).
If the task is impossible, return -1.

Example 1:
Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
Output: 3
Explanation: 
We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
Then, we can reconstruct the sporting event as follows:
We cut [1,9] into segments [1,2] + [2,8] + [8,9].
Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting
event [0, 10].

Example 2:
Input: clips = [[0,1],[1,2]], T = 5
Output: -1
Explanation: 
We can't cover [0,5] with only [0,1] and [0,2].

Example 3:
Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],
                [4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]],
       T = 9
Output: 3
Explanation: 
We can take clips [0,4], [4,7], and [6,9].

Example 4:
Input: clips = [[0,4],[2,8]], T = 5
Output: 2
Explanation: 
Notice you can have extra video after the event ends.

Note:
- 1 <= clips.length <= 100
- 0 <= clips[i][0], clips[i][1] <= 100
- 0 <= T <= 100
"""

class SolutionSortStartPrevEndAndEndGreedy(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int

        Time complexity: O(n*logn), where n is clips length.
        Space complexity: O(1).
        """
        # Sort clips by start.
        clips = sorted(clips)

        # Apply greedy algorithm to check (start, end) in prev_end and end.
        prev_end, end = -1, 0
        counter = 0

        for s, e in clips:
            if end >= T or s > end:
                # If reached T already or s falls behind end.
                break
            elif prev_end < s:
                # If s falls in between prev_end and end.
                counter += 1
                prev_end = end

            # Update end by new clip.
            end = max(end, e)

        # Check if end passes T.
        if end >= T:
            return counter
        else:
            return -1


class SolutionSortStartDPGreedy(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int

        Time complexity: O(n*logn+n*T), where n is clips length.
        Space complexity: O(T).
        """
        # Sort clips by start.
        clips = sorted(clips)

        # Create DP table dp, where dp[i] is min number of clips 
        # required to reach minute i.
        dp = [101] * 101
        dp[0] = 0

        for c in clips:
            for i in range(c[0] + 1, c[1] + 1):
                dp[i] = min(dp[i], dp[c[0]] + 1)

        if dp[T] >= T:
            # If dp at minute T is not updated.
            return -1
        else:
            return dp[T]


def main():
    # Output: 3
    clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
    T = 10
    print SolutionSortStartPrevEndAndEndGreedy().videoStitching(clips, T)
    print SolutionSortStartDPGreedy().videoStitching(clips, T)

    # Output: -1
    clips = [[0,1],[1,2]]
    T = 5
    print SolutionSortStartPrevEndAndEndGreedy().videoStitching(clips, T)
    print SolutionSortStartDPGreedy().videoStitching(clips, T)

    # Output: 3
    clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],
             [4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]]
    T = 9
    print SolutionSortStartPrevEndAndEndGreedy().videoStitching(clips, T)
    print SolutionSortStartDPGreedy().videoStitching(clips, T)

    # Output: 2
    clips = [[0,4],[2,8]]
    T = 5
    print SolutionSortStartPrevEndAndEndGreedy().videoStitching(clips, T)
    print SolutionSortStartDPGreedy().videoStitching(clips, T)


if __name__ == '__main__':
    main()
