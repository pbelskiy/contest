class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        idx = 0
        output = []

        # collect
        while idx < len(words):
            width = 0
            line = []

            while idx < len(words):
                if len(line) + width + len(words[idx]) > maxWidth:
                    break

                line.append(words[idx])
                width += len(words[idx])
                idx += 1

            # format
            spaces = maxWidth - width

            # last line
            if idx == len(words):
                pad = spaces - len(line) + 1
                output.append(' '.join(line) + ' ' * pad)
                continue

            i = 1
            count = len(line) - 1
            while spaces > 0:
                if count == 0:
                    pad = spaces
                else:
                    pad = math.ceil(spaces / count)

                spaces -= pad
                count -= 1
                line.insert(i, ' ' * pad)
                i += 2

            output.append(''.join(line))

        return output
