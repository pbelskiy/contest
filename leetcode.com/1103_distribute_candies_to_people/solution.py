class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        row = [0]*num_people
        x = 1

        while candies > 0:
            for i in range(num_people):
                if candies < x:
                    row[i] += candies
                    return row

                row[i] += x
                candies -= x
                x += 1

        return row
