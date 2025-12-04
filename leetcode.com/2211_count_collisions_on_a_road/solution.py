"""
Since only RL gives us +2 collisions, just replace them to S (static).
Then easily calculate rest of collisions.

TC: O(N)
SC: O(N)
"""
class Solution:
    def countCollisions(self, s: str) -> int:
        t = s.count('RL')*2
        s = s.replace('RL', 'S')

        # calc all `R` collisions
        for i in range(len(s) - 1, -1, -1):
            if s[i] != 'R':
                break
        for j in range(i):
            if s[j] == 'R':
                t += 1

        # calc all `L` collisions
        for i in range(len(s)):
            if s[i] != 'L':
                break
        for j in range(len(s) - 1, i, -1):
            if s[j] == 'L':
                t += 1

        return t

