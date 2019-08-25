"""Leetcode 160. Intersection of Two Linked Lists
Easy

URL: https://leetcode.com/problems/intersection-of-two-linked-lists/

Write a program to find the node at which the intersection of
two singly linked lists begins.

For example, the following two linked lists:

begin to intersect at node c1.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5],
skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8
(note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B,
it reads as [5,0,1,8,4,5].
There are 2 nodes before the intersected node in A;
There are 3 nodes before the intersected node in B. 

Example 2:
Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2
(note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [0,9,1,2,4].
From the head of B, it reads as [3,2,4].
There are 3 nodes before the intersected node in A;
There are 1 node before the intersected node in B.

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4].
From the head of B, it reads as [1,5].
Since the two lists do not intersect, intersectVal must be 0,
while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.

Notes:
- If the two linked lists have no intersection at all, return null.
- The linked lists must retain their original structure after the function returns.
- You may assume there are no cycles anywhere in the entire linked structure.
- Your code should preferably run in O(n) time and use only O(1) memory.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class SolutionTwoPointers(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode

        Time complexity: O(max(a, b)), where a and b is the lenght of lists A and B.
        Space complexity: O(1).
        """
        if not headA or not headB:
            return None

        # Two pointer method: Check current nodes are the same or not.
        currentA = headA
        currentB = headB

        while currentA != currentB:
            if currentA:
                # If not, visit next nodes.
                currentA = currentA.next
            else:
                # When arrive at the end, visit the head of another list.
                currentA = headB

            if currentB:
                currentB = currentB.next
            else:
                currentB = headA

        return currentA


def main():
    # Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5],
    # Output: Reference of the node with value = 8
    headA = ListNode(4)
    headA.next = ListNode(1)
    headB = ListNode(5)
    headB.next = ListNode(0)
    headB.next.next = ListNode(1)
    intersectNode1 = ListNode(8)
    intersectNode2 = ListNode(4)
    intersectNode3 = ListNode(5)

    headA.next.next = intersectNode1
    headA.next.next.next = intersectNode2
    headA.next.next.next.next = intersectNode3
    headB.next.next = intersectNode1
    headB.next.next.next = intersectNode2
    headB.next.next.next.next = intersectNode3  

    print SolutionTwoPointers().getIntersectionNode(headA, headB).val


if __name__ == '__main__':
    main()
