class Solution:
    def minimizeStringValue(self, s: str) -> str:
        def get(count):
            for k, _ in sorted(count.items(), key=lambda t: (t[1], t[0])):
                return k

        count = Counter(s)
        a = list(s)

        if '?' in count:
            del count['?']

        for ch in string.ascii_lowercase:
            if ch not in count:
                count[ch] = 0

        # get
        chars = []
        for i in range(len(a)):
            if a[i] == '?':
                chars.append(get(count))
                count[chars[-1]] += 1

        # lexicographically smallest
        chars = iter(sorted(chars))

        # replace
        for i in range(len(a)):
            if a[i] == '?':
                a[i] = next(chars)

        return ''.join(a)
