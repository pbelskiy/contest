class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        return sorted(friends, key=lambda i: order.index(i))

