class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        begin = list1
        b -= a - 1

        while a > 1:
            begin = begin.next
            a -= 1

        end = begin
        while b >= 0:
            end = end.next
            b -= 1

        begin.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = end
        return list1
