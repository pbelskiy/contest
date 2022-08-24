class LockingTree:

    def __init__(self, parent: List[int]):
        self.locked = [0]*len(parent)

        self.parent = parent
        self.childs = defaultdict(list)

        for i, p in enumerate(parent):
            self.childs[p].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num]:
            return False

        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] == user:
            self.locked[num] = 0
            return True

        return False

    def upgrade(self, num: int, user: int) -> bool:
        if self.locked[num]:
            return False

        # it has at least one locked descendant (by any user)
        q = deque([num])
        found = False
        while q:
            node = q.popleft()
            if self.locked[node]:
                found = True
                break

            q.extend(self.childs[node])

        if not found:
            return False

        # it does not have any locked ancestors
        q = deque([num])
        while q:
            node = q.popleft()
            if self.locked[node]:
                return False

            if self.parent[node] != -1:
                q.append(self.parent[node])

        # upgrade
        q = deque([num])
        while q:
            node = q.popleft()
            self.locked[node] = 0
            q.extend(self.childs[node])

        self.locked[num] = user
        return True
