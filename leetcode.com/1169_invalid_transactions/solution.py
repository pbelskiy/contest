Transaction = namedtuple('Transaction', ['time', 'amount', 'city', 'raw'])


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        names = defaultdict(list)
        for t in transactions:
            name, time, amount, city = t.split(',')
            names[name].append(Transaction(int(time), int(amount), city, t))

        invalid = []
        for times in names.values():
            times.sort()

            for i in range(len(times)):
                if int(times[i].amount) > 1000:
                    invalid.append(times[i].raw)
                    continue

                for j in range(len(times)):
                    if (abs(times[j].time - times[i].time) <= 60 and
                        times[j].city != times[i].city):
                        invalid.append(times[i].raw)
                        break

        return invalid
