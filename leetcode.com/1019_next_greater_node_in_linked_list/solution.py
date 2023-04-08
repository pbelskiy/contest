"""
Use monotonic stack here.

TC: O(N)
SC: O(N)

Example:
    [1,7,5,1,9,2,5,1]

    1 [] => 0
    5 [] => 0
    2 [5] => 5
    9 [] => 0
    1 [9] => 9
    5 [9] => 9
    7 [9] => 9
    1 [9, 7] => 7
"""
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        answer = []
        stack = []

        for n in reversed(values):

            while stack and stack[-1] <= n:
                stack.pop()

            if stack:
                answer.append(stack[-1])
            else:
                answer.append(0)

            # print(n, stack, '=>', answer[-1])
            stack.append(n)

        return answer[::-1]
