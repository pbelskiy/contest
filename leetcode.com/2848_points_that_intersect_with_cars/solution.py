class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda t: t[0])

        intervals = []
        begin, end = nums[0]

        for i in range(len(nums) - 1):
            if end + 1 >= nums[i + 1][0]:
                end = max(end, nums[i + 1][1])
                continue

            intervals.append([begin, end])
            begin, end = nums[i + 1]

        intervals.append([begin, end])

        total = 0
        for a, b in intervals:
            total += b - a + 1

        return total
