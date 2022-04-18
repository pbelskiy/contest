class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        def dfs(i):
            visited.add(i)

            for r in rooms[i]:
                if r not in visited:
                    dfs(r)

        visited = set()
        dfs(0)
        return len(visited) == len(rooms)
