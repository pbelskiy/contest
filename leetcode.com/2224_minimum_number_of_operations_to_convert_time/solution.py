class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        h1, m1 = map(int, current.split(':'))
        h2, m2 = map(int, correct.split(':'))
        d = abs((h1*60 + m1) - (h2*60 + m2))

        return (
            (d // 60) +           # 60
            ((d % 60) // 15) +    # 15
            (d % 60 % 15 // 5) +  # 5
            (d % 60 % 15 % 5)     # 1
        )
