class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        teams = {}

        for team in votes[0]:
            teams[team] = [0]*len(votes[0])

        for vote in votes:
            for i, team in enumerate(vote):
                teams[team][i] += 1

        result = list(teams.keys())
        result.sort(key=lambda k: (teams[k], -ord(k)), reverse=True)
        return ''.join(result)
