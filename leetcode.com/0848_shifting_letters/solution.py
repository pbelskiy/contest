class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total = sum(shifts)

        for i in range(len(shifts)):
            total -= shifts[i]
            shifts[i] = (shifts[i] + total) % 26

        string = []

        for i in range(len(shifts)):
            v = ord(s[i]) + shifts[i]
            if v > 0x7a:
                v = 0x60 + (v % 0x7a)

            string.append(chr(v))

        return ''.join(string)
