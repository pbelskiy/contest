"""
Bit manipulations.

Example: n = 7, x = 9

1) Use `x` as mask where set bits cannot be changed.
2) Use `n - 1` as target.

mask   = 1001 => _00_
target = 110

Then fill unset bit in mask by target bits from right to left.

  _00_ => 9  (1)
  _01_ => 11 (2)
  _10_ => 13 (3)
  _11_ => 15 (4)
 1_00_ => 25 (5)
 1_01_ => 17 (6)
 1_10_ => 29 (7) <- RESULT!

Target = 6 (7 - 1) becasue it's in binary form is 110. which shown above.
"""
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        if n == 1:
            return x

        mask = list('0'*30 + bin(x)[2:])
        right = len(mask) - 1

        for v in reversed(bin(n - 1)[2:]):
            while mask[right] == '1':
                right -= 1

            mask[right] = v
            right -= 1

        return int(''.join(mask), 2)
