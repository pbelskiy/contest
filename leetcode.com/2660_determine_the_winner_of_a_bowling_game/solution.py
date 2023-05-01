class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:

        def get_score(a):
            s = 0

            for i in range(len(a)):
                if (i >= 1 and a[i - 1] == 10) or (i >= 2 and a[i - 2] == 10):
                    s += a[i]*2
                else:
                    s += a[i]

            return s

        p1, p2 = get_score(player1), get_score(player2)

        if p1 > p2:
            return 1
        elif p2 > p1:
            return 2
        else:
            return 0
