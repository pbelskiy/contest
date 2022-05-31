class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        count = Counter()

        for i, message in enumerate(messages):
            count[senders[i]] += message.count(' ') + 1

        res = count.most_common()
        val = res[0][1]
        res = list(filter(lambda t: t[1] == val, res))
        res.sort(key=lambda t: t[0], reverse=True)
        return res[0][0]
