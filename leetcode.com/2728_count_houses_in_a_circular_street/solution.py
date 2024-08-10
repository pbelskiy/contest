"""
2728. Count Houses in a Circular Street (Easy)

You are given an object street of class Street that represents a
circular street and a positive integer k which represents a maximum
bound for the number of houses in that street (in other words, the
number of houses is less than or equal to k). Houses' doors could be
open or closed initially.

Initially, you are standing in front of a door to a house on this
street. Your task is to count the number of houses in the street.

The class Street contains the following functions which may help you:

void openDoor(): Open the door of the house you are in front of.
void closeDoor(): Close the door of the house you are in front of.
boolean isDoorOpen(): Returns true if the door of the current house is open and false otherwise.
void moveRight(): Move to the right house.
void moveLeft(): Move to the left house.
Return ans which represents the number of houses on this street.

Example 1:
Input: street = [0,0,0,0], k = 10
Output: 4
Explanation: There are 4 houses, and all their doors are closed.
The number of houses is less than k, which is 10.
"""
class Solution:
    def houseCount(self, street: Optional['Street'], k: int) -> int:
        for i in range(k):
            street.openDoor()
            street.moveRight()

        for i in range(k):
            street.moveLeft()

        street.closeDoor()
        street.moveRight()

        t = 0
        for i in range(k):
            if not street.isDoorOpen():
                break
            t += 1
            street.moveRight()

        return t + 1
