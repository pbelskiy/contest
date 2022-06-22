class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        return str(sorted(map(int, nums))[-k])
