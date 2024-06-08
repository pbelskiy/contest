class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        q = deque(list(range(n)))
        m = max(skills)

        leader, count = None, 0

        while True:
            a, b = q.popleft(), q.popleft()

            if skills[a] > skills[b]:
                q.appendleft(a)
                q.append(b)

                if leader == a:
                    count += 1
                else:
                    leader = a
                    count = 1
            else:
                q.appendleft(b)
                q.append(a)

                if leader == b:
                    count += 1
                else:
                    leader = b
                    count = 1

            if count == k or skills[leader] == m:
                return leader
