class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d = dict(
            type=0,
            color=1,
            name=2,
        )

        x = d[ruleKey]
        total = 0

        for item in items:
            if item[x] == ruleValue:
                total += 1

        return total
