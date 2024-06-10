class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count1 = Counter(s1.split(' '))
        count2 = Counter(s2.split(' '))

        uncommon = []

        for k, v in count1.items():
            if v == 1 and k not in count2:
                uncommon.append(k)

        for k, v in count2.items():
            if v == 1 and k not in count1:
                uncommon.append(k)

        return uncommon
