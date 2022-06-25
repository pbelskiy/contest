from graphlib import TopologicalSorter, CycleError


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = collections.defaultdict(list)
        for a, b in prerequisites:
            d[a].append(b)

        try:
            tuple(TopologicalSorter(d).static_order())
        except CycleError:
            return False

        return True
