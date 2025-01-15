class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        t = num2.bit_count()
        v = set()
        r = 0

        # greedy unset MSB
        for i in range(num1.bit_length(), -1, -1):
            if t == 0:
                break

            if (1 << i) & num1:
                num1 &= ~(1 << i)
                v.add(i)
                r |= (1 << i)
                t -= 1

        # greedy set rest of needed bits, LSB, ignore visited
        for i in range(32):
            if t == 0:
                break

            if i in v:
                continue

            r |= (1 << i)
            t -= 1

        return r
