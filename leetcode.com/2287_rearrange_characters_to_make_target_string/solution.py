class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        total = 0
        counter_s = Counter(s)
        counter_t = Counter(target)

        while counter_s >= counter_t:
            counter_s -= counter_t
            total += 1

        return total
