class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ops = []
        i = 1

        for t in target:

            while i != t:
                ops.extend(['Push', 'Pop'])
                i += 1

            ops.append('Push')
            i += 1

        return ops
