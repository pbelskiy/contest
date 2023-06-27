class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        t, h = 0, []

        left, left_p = 0, candidates
        right, right_p = len(costs) - 1, candidates

        while k > 0:

            # add from left
            for i in range(left_p):
                if left > right:
                    left_p = 0
                    break

                heappush(h, (costs[left], left, 'left'))
                left += 1
                left_p -= 1

            # add from right
            for i in range(right_p):
                if right < left:
                    right_p = 0
                    break

                heappush(h, (costs[right], right, 'right'))
                right -= 1
                right_p -= 1


            c, _, d = heappop(h)
            t += c
            k -= 1

            if d == 'right':
                right_p = 1
            else:
                left_p = 1

        return t
