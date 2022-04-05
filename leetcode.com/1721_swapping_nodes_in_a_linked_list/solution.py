class Solution:
    def swapNodes(self, head, k):
        p = []

        while head:
            p.append(head)
            head = head.next

        if len(p) == 1:
            return p[0]

        if k == len(p):
            k = 1

        p[k - 1], p[-k] = p[-k], p[k - 1]

        p[k - 1].next = p[k]
        p[k - 2].next = p[k - 1]

        p[-k].next = p[-k + 1]
        p[-k - 1].next = p[-k]

        p[-1].next = None

        return p[0]
