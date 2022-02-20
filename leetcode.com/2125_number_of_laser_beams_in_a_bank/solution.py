class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0

        bank = list(filter(lambda b: b.count('1') > 0, bank))

        if len(bank) == 1:
            return 0

        for row1, row2 in zip(bank, bank[1:]):
            total += row1.count('1') * row2.count('1')

        return total
