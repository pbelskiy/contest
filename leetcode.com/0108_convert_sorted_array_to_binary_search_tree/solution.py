class Solution:

    def build(self, nums):
        if len(nums) < 1:
            return None

        mid = len(nums) // 2

        node = TreeNode(
            nums[mid],
            self.build(nums[:mid]),
            self.build(nums[mid+1:]),
        )

        return node

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.build(nums)
