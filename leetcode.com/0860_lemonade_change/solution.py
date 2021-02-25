class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0

        for bill in bills:
            if bill == 5:
                five += 1
                continue

            if bill == 10:
                if five == 0:
                    return False

                five -= 1
                ten += 1
                continue

            if bill == 20:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                    continue

                elif five > 3:
                    five -= 3
                    continue

                return False

        return True

