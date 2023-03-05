class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        v = set()
        q = deque([start])
        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True

            for j in ((i + arr[i]), (i - arr[i])):
                if not (0 <= j < len(arr)):
                    continue

                if j not in v:
                    v.add(j)
                    q.append(j)

        return False
