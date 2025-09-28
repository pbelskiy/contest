class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        f = Counter(s)
        v = Counter(f.values())
        m = sorted(v.items(), key=lambda t: (-t[1], -t[0]))[0][0]

        return ''.join([k for k, v in f.items() if v == m])

