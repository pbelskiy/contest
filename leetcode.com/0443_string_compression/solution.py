class Solution:
    def compress(self, chars: List[str]) -> int:
        l, p, i, cnt = 0, 0, 0, 0

        while i < len(chars):

            # get count
            while i < len(chars) and chars[i] == chars[p]:
                cnt += 1
                i += 1

            # write char
            chars[l] = chars[p]
            l += 1

            # write count
            if cnt > 1:
                for n in str(cnt):
                    chars[l] = n
                    l += 1

            p = i
            cnt = 0

        return l
