class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = collections.defaultdict(int)

        for v in cpdomains:
            count, domain = v.split()

            d[domain] += int(count)
            for i in range(len(domain)):
                if domain[i] == '.':
                    d[domain[i+1:]] += int(count)

        domains = []

        for k, v in d.items():
            domains.append(f'{v} {k}')

        return domains
