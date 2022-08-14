class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        total = 0

        for count in Counter(tasks).values():
            if count == 1:
                return -1

            total += count // 3

            if count % 3 != 0:
                total += 1

        return total
