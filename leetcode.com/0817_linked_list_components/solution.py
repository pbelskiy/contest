class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        total = 0
        count = 0

        nums = set(nums)
        while head:
            if head.val in nums:
                count += 1
            else:
                if count > 0:
                    total += 1

                count = 0

            head = head.next

        if count > 0:
            total += 1

        return total
