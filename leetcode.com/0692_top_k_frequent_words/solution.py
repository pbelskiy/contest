class Solution:
    def topKFrequent(self, words, k):           
        count = list(Counter(words).items())
        count.sort(key=lambda t: (-t[1], t[0]))
        return [t[0] for t in count][:k]
