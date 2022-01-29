class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        idx = datetime.datetime(year=year, month=month, day=day).weekday()
        return week[idx]
