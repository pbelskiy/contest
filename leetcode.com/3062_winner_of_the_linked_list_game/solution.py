"""
3062. Winner of the Linked List Game (Easy)

You are given the head of a linked list of even length
containing integers.

Each odd-indexed node contains an odd integer and each
even-indexed node contains an even integer.

We call each even-indexed node and its next node a pair,
e.g., the nodes with indices 0 and 1 are a pair, the nodes
with indices 2 and 3 are a pair, and so on.

For every pair, we compare the values of the nodes in the pair:

If the odd-indexed node is higher, the "Odd" team gets a point.
If the even-indexed node is higher, the "Even" team gets a point.
Return the name of the team with the higher points, if the points
are equal, return "Tie".

Example 1:

Input:   head = [2,1]
Output:   "Even"

Explanation: There is only one pair in this linked list and that is (2,1). Since 2 > 1, the Even team gets the point.

Hence, the answer would be "Even".
"""
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        odd, even = 0, 0

        while head:
            if head.val > head.next.val:
                even += 1
            else:
                odd += 1

            head = head.next.next

        if odd == even:
            return 'Tie'

        if odd > even:
            return 'Odd'

        return 'Even'
