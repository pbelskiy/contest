class Solution:
    def countRotations(self, s: str, k: int) -> int:
        t = 0
        q = deque(list(s))

        for _ in range(len(s)):
            a = 0

            for i in range(len(q) - 1):
                if q[i] == q[i + 1]:
                    a += 1
            
            if a == k:
                t += 1

            q.append(q.popleft())

        return t

