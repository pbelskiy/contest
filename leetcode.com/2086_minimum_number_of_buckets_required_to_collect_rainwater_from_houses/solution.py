class Solution:
    def minimumBuckets(self, street: str) -> int:
        if (street[0] == 'H' and len(street) == 1) or street.startswith('HH') or street.endswith('HH') or 'HHH' in street:
            return -1

        return street.replace('H.H', 'XBX').replace('.H', 'BX').replace('H.', 'XB').count('B')
