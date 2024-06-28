class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        t = 0
        if sum(energy) >= initialEnergy:
            t += sum(energy) - initialEnergy + 1

        for i in range(len(experience)):
            if experience[i] >= initialExperience:
                d = experience[i] - initialExperience + 1
                t += d
                initialExperience += d

            initialExperience += experience[i]

        return t
