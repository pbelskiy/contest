class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def get_waviness(n):
            a = list(map(int, str(n)))
            t = 0
            for i in range(1, len(a) - 1):
                if a[i - 1] < a[i] > a[i + 1]:
                    t += 1
                elif a[i - 1] > a[i] < a[i + 1]:
                    t += 1

            return t

        t = 0
        for n in range(num1, num2 + 1):
            t += get_waviness(n)
        
        return t

