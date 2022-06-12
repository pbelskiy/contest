class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        count = Counter()

        for a, b in adjacentPairs:
            count[a] += 1
            count[b] += 1

            graph[a].append(b)
            graph[b].append(a)

        v, _ = count.most_common()[-1]

        array = []
        visited = set()

        while True:
            array.append(v)
            visited.add(v)

            for n in graph[v]:
                if n not in visited:
                    v = n
                    break
            else:
                break

        return array
