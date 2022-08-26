class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        def get_seconds(time):
            hours, minutes = map(int, time.split(':'))
            return (hours*60 + minutes)*60

        visits = defaultdict(list)

        for name, time in zip(keyName, keyTime):
            visits[name].append(time)

        names = []
        for name, times in visits.items():
            if len(times) < 3:
                continue

            times.sort()
            for i in range(0, len(times) - 2):
                if get_seconds(times[i + 2]) - get_seconds(times[i]) <= 60*60:
                    names.append(name)
                    break

        return sorted(names)
