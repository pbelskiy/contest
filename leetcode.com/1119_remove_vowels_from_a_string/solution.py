"""
1119. Remove Vowels from a String (Easy)

Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it,
and return the new string.

Example 1:
    Input: s = "leetcodeisacommunityforcoders"
    Output: "ltcdscmmntyfrcdrs"

Example 2:
    Input: s = "aeiou"
    Output: ""
"""
class Solution:
    def removeVowels(self, s: str) -> str:
        return s.replace('a', '') \
                .replace('e', '') \
                .replace('i', '') \
                .replace('o', '') \
                .replace('u', '')
