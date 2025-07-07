class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid = []

        for c, b, a in zip(code, businessLine, isActive):
            p = re.findall('(\w+)', c)
            if not p or p[0] != c:
                continue

            if b not in ("electronics", "grocery", "pharmacy", "restaurant"):
                continue

            if not a:
                continue

            valid.append((c, b, a))

        valid.sort(key=lambda t: (t[1], t[0]))
        return [v[0] for v in valid]

