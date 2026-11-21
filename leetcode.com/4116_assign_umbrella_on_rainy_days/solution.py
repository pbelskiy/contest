class Solution:
    def assignUmbrella(self, rain: list[int]) -> list[str]:
        answer = []
        freq = Counter()

        for i in range(len(rain)):
            alice = (i < len(rain) - 1 and rain[i] == rain[i + 1] == 1)
            bob = (rain[i] == 1)

            if alice and bob:
                if freq['Alice'] > freq['Bob']:
                    alice = False
                else:
                    bob = False

            if alice:
                freq['Alice'] += 1
                answer.append('Alice')
            elif bob:
                freq['Bob'] += 1
                answer.append('Bob')
            else:
                answer.append("None")

        return answer

