class Solution:
    def solve(self, S: str, pos: int) -> None:
        for i, ch in enumerate(S):
            if i < pos or ch.isdigit():
                continue

            newS = S[:i] + ch.upper() + S[i + 1:]
            self.cases.add(newS)
            self.solve(newS, i + 1)

            newS = S[:i] + ch.lower() + S[i + 1:]
            self.cases.add(newS)
            self.solve(newS, i + 1)

    def letterCasePermutation(self, S: str) -> List[str]:
        self.cases = set()
        self.solve(S, 0)
        
        if len(self.cases) == 0:
            self.cases.add(S)
        
        return self.cases

