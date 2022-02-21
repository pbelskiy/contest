class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []

        nums = [2]

        s = 2
        n = 4

        while True:
            if s + n > finalSum:
                break

            nums.append(n)
            s += n
            n += 2

        nums[-1] += finalSum - s
        return nums
