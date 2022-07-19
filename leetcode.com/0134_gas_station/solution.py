class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        def trace(i):
            tank, j = gas[i], i
            rest = len(gas)

            while tank > 0 and rest > 0:
                if j + 1 == len(gas):
                    j = -1

                tank -= cost[j]
                if tank < 0:
                    break
                tank += gas[j + 1]

                j += 1
                rest -= 1

            return rest == 0, j

        if sum(gas) < sum(cost):
            return -1

        visited = set()
        last = -1
        while last not in visited:
            visited.add(last)
            r, j = trace(last + 1)
            if r:
                return j
            last = j

        return -1
