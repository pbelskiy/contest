class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        count = Counter()
        nums = list(range(1, n + 1))*100

        j = rounds[0] - 1
        for i in range(len(rounds) - 1):

            while nums[j] != rounds[i + 1]:
                count[nums[j]] += 1
                j += 1

            count[nums[j]] += 1
            j += 1

        return sorted([k for k, v in count.items() if v == max(count.values())])
