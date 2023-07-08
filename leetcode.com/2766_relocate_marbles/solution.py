class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        positions = set(nums)

        for src, dst in zip(moveFrom, moveTo):
            positions.remove(src)
            positions.add(dst)

        return sorted(positions)
