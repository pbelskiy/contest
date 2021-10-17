class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def build(nums):
            if not nums:
                return

            i = nums.index(max(nums))
            return TreeNode(nums[i], build(nums[:i]), build(nums[i+1:]))

        return build(nums)
