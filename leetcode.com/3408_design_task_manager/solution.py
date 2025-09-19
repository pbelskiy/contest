"""
Use lazy remove.

TC: O(NlgN)
SC: O(N)
"""
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.h = []  # heap
        self.u = {}  # task -> user
        self.p = {}  # task -> priority

        for u, t, p in tasks:
            self.add(u, t, p)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heappush(self.h, (-priority, -taskId, userId))
        self.u[taskId] = userId
        self.p[taskId] = priority

    def edit(self, taskId: int, newPriority: int) -> None:
        if self.p[taskId] == newPriority:
            return

        userId = self.u[taskId]
        self.rmv(taskId)
        self.add(userId, taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        del self.u[taskId]
        del self.p[taskId]

    def execTop(self) -> int:
        while self.h:
            p, t, u = heappop(self.h)

            t = -t
            p = -p

            if t not in self.u:
                continue

            if self.u[t] != u:
                continue

            if self.p[t] != p:
                continue

            self.rmv(t)
            return u

        return -1

