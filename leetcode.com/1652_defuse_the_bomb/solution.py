class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        answer = [0]*len(code)

        for i in range(len(code)):
            if k > 0:
                if i + k >= len(code):
                    rest = (i + k + 1) % len(code)
                else:
                    rest = 0

                answer[i] = sum(code[i+1:i+k+1] + code[:rest])
            elif k < 0:
                answer[i] = sum([code[i - j] for j in range(-k, 0, -1)])
            else:
                answer[i] = 0

        return answer
