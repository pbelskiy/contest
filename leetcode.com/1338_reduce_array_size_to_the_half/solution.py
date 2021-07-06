class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr) // 2
        total = 0
        count = 0

        for k, v in Counter(arr).most_common():
            total += v
            count += 1

            if total >= n:
                break

        return count
