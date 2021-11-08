class Solution:
    def lengthLongestPath(self, s: str) -> int:
        stack = [('', 0, -1)]
        prev_length = 0
        prev_level = -1
        best = 0

        n = len(s)
        p = 0

        while p < n:
            level = 0
            while p < n and s[p] == '\t':
                level += 1
                p += 1

            name = ''
            while p < n and s[p] not in ('\t', '\n'):
                name += s[p]
                p += 1

            while p < n and s[p] == '\n':
                p += 1

            if level > prev_level and '.' not in name:
                length = prev_length + len(name) + 1
                stack.append((name, length, level))
                _, prev_length, prev_level = stack[-1]

            else:
                while level <= prev_level and len(stack) > 0:
                    prev_name, prev_length, prev_level = stack.pop()

                    if prev_level < level:
                        stack.append((prev_name, prev_length, prev_level))
                        break

                if level > prev_level and '.' not in name:
                    length = prev_length + len(name) + 1
                    stack.append((name, length, level))
                    _, prev_length, prev_level = stack[-1]

            if '.' in name:
                best = max(best, prev_length + len(name))

        return best
