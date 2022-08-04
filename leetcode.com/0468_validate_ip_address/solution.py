class Solution:

    def isV4(self, queryIP):
        for part in queryIP.split('.'):
            if not part.isdigit():
                return False
            if not (0 <= int(part) <= 255):
                return False
            if len(part) > 1 and part[0] == '0':
                return False

        return True

    def isV6(self, queryIP):
        for part in queryIP.split(':'):
            if not (1 <= len(part) <= 4):
                return False
            try:
                int(part, 16)
            except ValueError:
                return False

        return True

    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.count('.') == 3 and self.isV4(queryIP):
            return 'IPv4'

        if queryIP.count(':') == 7 and self.isV6(queryIP):
            return 'IPv6'

        return 'Neither'
