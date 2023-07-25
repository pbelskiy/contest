"""
Since maximum powers length is limited by number of bits of n (10**9)
so it's 29 powers. Doing brute force here is okay. It takes 700 ms for
worse test case when n = 536870911 ('0b11111111111111111111111111111')
and queries length is 10**5.

TC: O(N) [29N]
SC: O(N) [answers len]
"""
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = [2**i for i in range(n.bit_length()) if n & (1 << i)]

        answers = []
        for left, right in queries:
            v = 1
            for i in range(left, right + 1):
                v *= powers[i]

            answers.append(v % (10**9 + 7))

        return answers
