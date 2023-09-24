class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = Counter(s)
        if count['1'] == 1:
            return '0'*count['0'] + '1'

        return (count['1'] - 1)*'1' +  '0'*count['0'] + '1'
