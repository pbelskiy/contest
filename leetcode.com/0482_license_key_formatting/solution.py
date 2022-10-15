class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        d, m = divmod(len(s), k)

        parts = []

        if m:
            parts.append(s[:m])

        for i in range(len(s) // k):
            parts.append(s[m+i*k:m+(i+1)*k])

        return '-'.join(parts)
