class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait = 0

        for i in range(len(customers)):
            t = customers[i][1]

            if i == 0:
                d = 0
            else:
                d = max(0, sum(customers[i - 1]) - customers[i][0])

            wait += t + d
            customers[i][0] += d

        return wait / len(customers)
