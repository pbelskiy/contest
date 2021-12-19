class Solution:
    def minDeletions(self, s: str) -> int:
        total, used = 0, set()

        for cnt in collections.Counter(s).values():
            while cnt in used:
                cnt -= 1
                total += 1

                if cnt == 0:
                    break

            used.add(cnt)

        return total
