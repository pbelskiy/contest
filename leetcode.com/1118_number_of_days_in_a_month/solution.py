class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0) and month == 2:
            return 29

        return {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }[month]
