class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        
        def is_possible(curr):
            if len(curr) == 1:
                return True

            p = []
            for i in range(len(curr) - 1):
                s = curr[i:i+2]
                if s not in d:
                    return False
                p.append(d[s])

            for comb in product(*p):
                if is_possible(''.join(comb)):
                    return True
 
            return False

        d = defaultdict(list)
        for s in allowed:
            d[s[:2]].append(s[-1])

        return is_possible(bottom)

