class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        heapify(hand)

        while hand:
            s = groupSize - 1
            a = heappop(hand)
            r = []

            while hand and s > 0:
                b = heappop(hand)
                if b - 1 == a:
                    s -= 1
                    a = b
                else:
                    r.append(b)

            if s != 0:
                return False

            for v in r:
                heappush(hand, v)

        return True
