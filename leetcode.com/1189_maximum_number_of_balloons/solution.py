class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        total = 0
        count = collections.Counter(text)

        while True:
            if count.get('b', 0) > 0:
                count['b'] -= 1
            else:
                break

            if count.get('a', 0) > 0:
                count['a'] -= 1
            else:
                break

            if count.get('l', 0) > 1:
                count['l'] -= 2
            else:
                break

            if count.get('o', 0) > 1:
                count['o'] -= 2
            else:
                break

            if count.get('n', 0) > 0:
                count['n'] -= 1
            else:
                break

            total += 1

        return total
