class Solution:
    def kMirror(self, k: int, n: int) -> int:
 
        def get_mirror():
            s = ['1']
            i = 0
            j = 0

            while True:
                yield int(''.join(s))

                # global overflow
                if list(set(s)) == ['9']:
                    if len(s) == 1:
                        s = ['1', '1']
                        i = 0
                        j = 1
                    else:
                        s = ['1'] + ['0']*(len(s) - 1) + ['1']
                        if len(s) % 2 == 0:
                            i = len(s) // 2 - 1
                            j = len(s) // 2
                        else:
                            i = j = len(s) // 2

                    continue

                # local overflow
                local_overflow = False

                if s[i] == s[j] == '9':
                    local_overflow = True

                    i_save = i
                    j_save = j

                    while s[i] == s[j] == '9':
                        s[i] = '0'
                        s[j] = '0'
                        i -= 1
                        j += 1

                # increase
                if i == j:
                    s[i] = str(int(s[i]) + 1)
                else:
                    s[i] = str(int(s[i]) + 1)
                    s[j] = str(int(s[j]) + 1)

                if local_overflow:
                    i = i_save
                    j = j_save

        def to_base(n):
            if n == 0:
                return '0'
            digits = []
            while n > 0:
                n, rem = divmod(n, k)
                digits.append(str(rem))
            return ''.join(reversed(digits))

        total = 0

        g = get_mirror()
        while n > 0:
            x = next(g)
            converted = to_base(x)
            if str(converted) == str(converted)[::-1]:
                total += x
                n -= 1

        return total

