class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0

        angle_hours = (hour + minutes / 60)*30
        angle_minutes = minutes*6

        return min(
            abs(angle_hours - angle_minutes),
            360 - abs(angle_hours - angle_minutes)
        )
