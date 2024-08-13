class Solution:
    def toHexspeak(self, num: str) -> str:
        s = hex(int(num))[2:].replace('0', 'O').replace('1', 'I').upper()
        if set(s) - {'A', 'B', 'C', 'D', 'E', 'F', 'I', 'O'}:
            return 'ERROR'
        return s
