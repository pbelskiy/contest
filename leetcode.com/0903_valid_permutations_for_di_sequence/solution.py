import itertools


class Solution:
    def numPermsDISequence(self, S: str) -> int:
        count = 0

        for variant in itertools.permutations(range(len(S) + 1)):
            print(variant)
            for c, a, b in zip(S, variant, variant[1:]):
                if c == 'D' and a < b:
                    break
                if c == 'I' and a > b:
                    break
            else:
                count += 1

        return count


if __name__ == '__main__':
    print(Solution().numPermsDISequence('ID'), 2)
    # print(Solution().numPermsDISequence('DID'), 5)
    # print(Solution().numPermsDISequence('IIDDIDIDDI'), 96381)
