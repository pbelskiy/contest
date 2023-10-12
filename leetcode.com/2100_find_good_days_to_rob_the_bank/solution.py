class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:

        @cache
        def get_left(i):
            if i - 1 >= 0 and security[i - 1] >= security[i]:
                return get_left(i - 1) + 1
            return 0

        @cache
        def get_right(i):
            if i + 1 < len(security) and security[i] <= security[i + 1]:
                return get_right(i + 1) + 1
            return 0

        days = []
        for i in range(time, len(security) - time):
            if get_left(i) >= time and get_right(i) >= time:
                days.append(i)

        return days
