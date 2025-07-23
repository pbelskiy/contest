class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:

        @cache
        def dfs(s, p1):
            states.add(s)

            # check if win state
            for i in range(0, 9, 3):
                if s[i:i+3] in win:
                    return

            for i in range(3):
                if s[i] + s[i+3] + s[i+6] in win:
                    return

            if s[0] + s[4] + s[8] in win:
                return
            if s[6] + s[4] + s[2] in win:
                return

            # make move
            for i in range(9):
                if s[i] == ' ':
                    ch = 'X' if p1 else 'O'
                    ns = s[:i] + ch + s[i+1:]
                    dfs(ns, not p1)

        win = ('X'*3, 'O'*3)
        states = set()
        dfs(" "*9, True)
        return ''.join(board) in states

