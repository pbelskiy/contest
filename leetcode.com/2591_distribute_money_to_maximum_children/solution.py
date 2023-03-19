class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # everyone must receive at least 1 dollar
        extra = money - children
        if extra < 0:
            return -1

        t = 0

        # gives additional 7 dollars to everyone
        while extra >= 7 and t < children:
            extra -= 7
            t += 1

        # there is extra dollars, so latest recieve more
        if extra > 0 and t == children:
            t -= 1

        # nobody receives 4 dollars.
        elif extra == 3 and children - t == 1:
            t -= 1

        return t
