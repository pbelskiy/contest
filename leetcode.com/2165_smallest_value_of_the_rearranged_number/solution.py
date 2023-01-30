class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            a = sorted(str(abs(num)))
            if a[0] == '0':
                for i in range(len(a)):
                    if a[i] != '0':
                        a[0], a[i] = a[i], a[0]
                        break

            return int(''.join(a))

        a = sorted(str(abs(num)), reverse=True)
        return int('-' + ''.join(a))
