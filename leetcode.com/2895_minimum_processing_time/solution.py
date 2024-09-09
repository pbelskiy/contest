class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)

        score = 0
        j = 0

        for i in range(0, len(tasks), 4):
            score = max(score, processorTime[j] + max(tasks[i:i+4]))
            j += 1

        return score
