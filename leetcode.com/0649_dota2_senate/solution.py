class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d, r = 0, 0
        count, queue = Counter(senate), deque(senate)

        while queue and count['D'] > 0 and count['R'] > 0:
            s = queue.popleft()

            if s == 'R':
                if r > 0:
                    count['R'] -= 1
                    r -= 1
                else:
                    queue.append(s)
                    d += 1

            if s == 'D':
                if d > 0:
                    count['D'] -= 1
                    d -= 1
                else:
                    queue.append(s)
                    r += 1

        return 'Radiant' if count['R'] > 0 else 'Dire'
