class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        total, i, j = 0, 0, 0

        while i < len(players) and j < len(trainers):

            if players[i] <= trainers[j]:
                i += 1
                total += 1

            j += 1

        return total
