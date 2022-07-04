class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {' ': ' '}

        new_key = []

        for k in key:
            if k == ' ':
                continue
            if k in new_key:
                continue
            new_key.append(k)

        for i in range(26):
            d[new_key[i]] = chr(ord('a') + i)

        return ''.join([d[m] for m in message])
