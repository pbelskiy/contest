# https://pbelskiy.medium.com/z-функция-8fd2654754eb

def z_func(s):
    z = [0]*len(s)

    l, r = 0, 0

    for i in range(1, len(s)):
        # use previous info to optimize search
        if i <= r:
            z[i] = min(
                z[i - l],  # previous prefix
                r - i + 1  # remain characters in range
            )

        # increase step by step
        while i + z[i] < len(s) and s[i + z[i]] == s[z[i]]:
            z[i] += 1

        # increase r
        if z[i] > 0 and i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1

    return z


def find_substring(s, p):
    z = z_func(p + '#' + s)
    result = []
    for i in range(len(z)):
        if z[i] == len(p):
            result.append(i - len(p) - 1)

    return result


s = 'abacabaaba'
p = 'aba'
print(find_substring(s, p))  # [0, 4, 7]
