"""
Greedy solution

TC: O(N)
SC: O(1)
"""
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        q = deque()
        i = 0

        very_first = None
        very_last = None

        shortest = float('inf')

        while head:
            i += 1

            q.append(head.val)
            head = head.next

            while len(q) > 3:
                q.popleft()

            if len(q) != 3:
                continue

            if not ((q[0] < q[1] > q[2]) or (q[0] > q[1] < q[2])):
                continue

            # save very first value
            if not very_first:
                very_first = i

            if very_last:
                shortest = min(shortest, i - very_last)

            # save very last value
            very_last = i

        if not very_first or shortest == float('inf'):
            return [-1, -1]

        return [min(shortest, very_last - very_first), very_last - very_first]
