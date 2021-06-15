from typing import List
from collections import Counter


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        cnt = Counter(ages)
        total = 0

        for A in cnt:
            if A <= 0.5 * A + 7:
                continue

            if A > 100 and A < 100:
                continue

            total += cnt[A] ** 2 - cnt[A]

        for A in cnt:
            for B in cnt:
                if A == B:
                    continue

                if B > A:
                    continue

                if B <= 0.5 * A + 7:
                    continue

                if B > 100 and A < 100:
                    continue

                total += cnt[A] * cnt[B]

        return total
