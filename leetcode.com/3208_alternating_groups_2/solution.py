"""
Simplify sliding window by using helper array
of alternating values.

TC: O(N)
SC: O(N)
"""
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        a = []

        for i in range(len(colors) - 1):
            a.append(colors[i] != colors[i+1])

        a.append(colors[-1] != colors[0])
        a *= 2
        k -= 1

        t = 0
        freq = Counter(a[:k])

        if freq[False] == 0:
            t += 1

        left = 0
        for right in range(k, len(a) // 2 + k - 1):
            freq[a[left]] -= 1
            freq[a[right]] += 1
            
            left += 1

            if freq[False] == 0:
                t += 1
        
        return t

