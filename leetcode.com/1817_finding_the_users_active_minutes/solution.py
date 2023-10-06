class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        users = defaultdict(set)
        for uid, minute in logs:
            users[uid].add(minute)

        uams = defaultdict(int)
        for v in users.values():
            uams[len(v)] += 1

        answer = []
        for j in range(1, k + 1):
            answer.append(uams[j])

        return answer
