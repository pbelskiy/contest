"""
Sort and check prefix of previous folder.

TC: O(sort)
SC: O(sort)
"""
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        answer = []

        for f in sorted(folder):
            if not (answer and f.startswith(answer[-1] + '/')):
                answer.append(f)

        return answer

