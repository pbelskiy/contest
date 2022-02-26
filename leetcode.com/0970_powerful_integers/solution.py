class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound == 0:
            return []

        values = set()

        im = int(math.log(bound, x)) + 1 if x > 1 else 1
        jm = int(math.log(bound, y)) + 1 if y > 1 else 1

        for i in range(im):
            for j in range(jm):
                n = x**i + y**j
                if n > bound:
                    break
                values.add(n)

        return values
