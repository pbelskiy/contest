class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = Counter()

        left = 0
        right = 0
        res = 0

        while right < len(fruits):

            if fruits[right] in count or len(count.keys()) < 2:
                count[fruits[right]] += 1
                right += 1

            else:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

            res = max(res, right - left)

        return res
