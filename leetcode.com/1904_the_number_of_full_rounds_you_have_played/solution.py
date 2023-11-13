class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        if loginTime == logoutTime:
            return 0

        h1, m1 = map(int, loginTime.split(':'))
        h2, m2 = map(int, logoutTime.split(':'))

        if (h1*60 + m1) >= (h2*60 + m2):
            return self.numberOfRounds(loginTime, '24:00') + \
                   self.numberOfRounds('00:00', logoutTime)

        # increase to closest
        if m1 % 15 != 0:
            m1 += 15 - m1 % 15

        # reduce to closest
        if m2 % 15 != 0:
            m2 -= m2 % 15

        return max(0, (h2*60 + m2) - (h1*60 + m1)) // 15
