"""
Sliding window.

Example: `abcabc`
    ___
    abcabc +1
     ___
    abcabc +2
      ___
    abcabc +3
       ___
    abcabc +4

Each time when we met conditions we add to `total` vairable
`left` variable because we build up more valid array if go
back left.

Answer: 10

TC: O(N)
SC: O(1)
"""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        f = {'a': 0, 'b': 0, 'c': 0}
        t = 0

        left = 0
        for right in range(len(s)):
            f[s[right]] += 1

            while all(f.values()):
                f[s[left]] -= 1
                left += 1

            t += left  # curr valid array and we can increase to left

        return t
