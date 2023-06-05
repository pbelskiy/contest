class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        diff_a = []
        diff_b = []

        for a, b in zip(s, goal):
            if a != b:
                diff_a.append(a)
                diff_b.append(b)

        if len(diff_a) > 2:
            return False

        if len(diff_a) == 0:
            return len(s) != len(set(s))

        return sorted(diff_a) == sorted(diff_b)
