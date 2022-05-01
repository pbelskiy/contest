class Solution:
    def countValidWords(self, sentence: str) -> int:
        total = 0

        for w in sentence.split(' '):
            if not w:
                continue

            if set('0123456789') & set(w):
                continue

            if '-' in w:
                cnt = collections.Counter(w)
                if cnt['-'] > 1:
                    continue

                if w[0] == '-' or w[-1] == '-':
                    continue

            if set('!.,') & set(w):
                cnt = collections.Counter(w)
                if (cnt['!'] + cnt['.'] + cnt[',']) > 1:
                    continue

                if w[-1] not in ('!', '.', ','):
                    continue

            if '-,' in w or '-!' in w or '-.' in w:
                continue

            total += 1
            # print(total, w)

        return total
