"""
Simulate process due to small restrictions.

TC: O(sort(N)*NM)
SC: O(N)
"""
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda t: (int(t[1]), t[0] == 'MESSAGE'))

        online = [0]*numberOfUsers
        mentions = [0]*numberOfUsers

        for e, t, s in events:
            if e == 'OFFLINE':
                online[int(s)] = int(t) + 60
                continue

            if s == 'ALL':
                for i in range(numberOfUsers):
                    mentions[i] += 1

            elif s == 'HERE':
                for i in range(numberOfUsers):
                    if online[i] <= int(t):
                        mentions[i] += 1

            else:
                for i in re.findall(r'(\d+)', s):
                    mentions[int(i)] += 1

        return mentions
