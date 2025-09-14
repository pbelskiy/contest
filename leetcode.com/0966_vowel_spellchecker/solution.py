"""
Make three hashmap for fast lookup.

TC: O(N)
SC: O(N)
"""
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        def replace_vowels(w):
            s = ''
            for ch in w.lower():
                if ch in {'a', 'e', 'i', 'o', 'u'}:
                    s += '#'
                else:
                    s += ch

            return s

        wordlist_set = set(wordlist)
        wordlist_cap = {}
        wordlist_vow = {}

        for w in reversed(wordlist):
            wordlist_cap[w.lower()] = w
            wordlist_vow[replace_vowels(w)] = w

        answer = []
        for q in queries:
            # exactly matches
            if q in wordlist_set:
                answer.append(q)
                continue

            # matches a word up to capitlization
            if q.lower() in wordlist_cap:
                answer.append(wordlist_cap[q.lower()])
                continue

            # matches a word up to vowel errors
            s = replace_vowels(q)
            if s in wordlist_vow:
                answer.append(wordlist_vow[s])
                continue

            # no matches
            answer.append('')

        return answer

