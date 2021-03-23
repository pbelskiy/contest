# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        l = 0
        node = root

        while node:
            node = node.next
            l += 1

        b = 0   # big block size
        bc = 0  # big block count

        if k > l:
            a = 1
            ac = k
        elif l % k == 0:
            a = l / k
            ac = k
        else:
            a = math.floor(l / k)
            b = math.ceil(l / k)

            if b * (k-1) + a == l:
                bc = k - 1
                ac = 1
            else:
                ac = k - 1
                bc = 1

                while b * bc + a * ac != l:
                    bc += 1
                    ac -= 1

        # construct
        splited = []
        node = root

        # print(b, bc, a, ac)

        for block_size, blocks_count in ((b, bc), (a, ac)):
            for _ in range(blocks_count):
                curr_size = 0
                sln = None
                slr = None

                while node and curr_size < block_size:
                    if not slr:
                        slr = ListNode(node.val)
                        sln = slr
                    else:
                        sln.next = ListNode(node.val)
                        sln = sln.next

                    curr_size += 1
                    node = node.next

                splited.append(slr)

        return splited

