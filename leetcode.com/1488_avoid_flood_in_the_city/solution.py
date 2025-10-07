class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        last = {}
        dry = []
        answer = [-1]*len(rains)

        for i in range(len(rains)):
            # save dry day
            if rains[i] == 0:
                dry.append(i)
                continue

            # fill our empty lake, and save it's day
            if rains[i] not in last:
                last[rains[i]] = i
                continue

            # it's already full, can we dry?
            for j in range(len(dry)):
                # first day after previous full
                if dry[j] > last[rains[i]]:
                    answer[dry[j]] = rains[i]
                    dry.pop(j)
                    last[rains[i]] = i
                    break
            else:
                return []

        # fill unused dry days by any lake, e.g. 1
        for j in range(len(dry)):
            answer[dry[j]] = 1

        return answer

