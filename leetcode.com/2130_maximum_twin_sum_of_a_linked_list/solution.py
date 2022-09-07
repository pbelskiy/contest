class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []

        while head:
            values.append(head.val)
            head = head.next

        twin_max_sum = 0

        left, right = 0, len(values) - 1
        while left < right:
            twin_max_sum = max(twin_max_sum, values[left] + values[right])
            left += 1
            right -= 1

        return twin_max_sum
