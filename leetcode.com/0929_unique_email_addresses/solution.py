class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniques = set()

        for e in emails:
            local, domain = e.split('@')

            if '+' in local:
                local = local.split('+')[0]
            local = local.replace('.', '')

            uniques.add(f'{local}@{domain}')

        return len(uniques)
