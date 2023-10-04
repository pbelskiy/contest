class Solution:
    def dayOfYear(self, date: str) -> int:
        d1 = datetime.datetime.strptime(date, r'%Y-%m-%d')
        d2 = datetime.datetime.strptime(date.split('-')[0] + '-01-01', r'%Y-%m-%d')
        return (d1 - d2).days + 1
