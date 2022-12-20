class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        c1 = complex(num1.replace('i', 'j').replace('+-', '-'))
        c2 = complex(num2.replace('i', 'j').replace('+-', '-'))

        c3 = c1*c2
        return f'{int(c3.real)}+{int(c3.imag)}i'
