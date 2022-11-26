class Solution:
    def bestClosingTime(self, customers: str) -> int:
        v = [0]*len(customers)
        r = [0]*(len(customers) + 1)
        s = 0

        for i in range(len(customers)):
            v[i] = int(customers[i] == 'Y')
            s += v[i]

        r[0] = s
        for j in range(len(customers)):
            if customers[j] == 'Y':
                r[j + 1] = r[j] - 1
            else:
                r[j + 1] = r[j] + 1

        m = min(r)
        for i in range(len(r)):
            if r[i] == m:
                return i
