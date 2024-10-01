"""
Here we group all numbers by reminder of k.

Then as we can see how can we join groups.
For example for numbers with remainder = 2
we can use numbers with remainder 3 and so
on, except reminder 0 which is special case.

So then just check the count numbers in each
group is enought.

Example (k = 5):
  Reminder   List       List (k - reminder)
     0      [5, 10]    []
     1      [1, 6]     [4, 9]
     2      [2, 7]     [3, 8]
     3      [3, 8]     [2, 7]
     4      [4, 9]     [1, 6]

TC: O(N)
SC: O(N)
"""
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = defaultdict(list)
        for n in arr:
            d[n % k].append(n)

        for r, v in d.items():
            if r == 0:
                if len(v) % 2 != 0:
                    return False
                continue

            if len(d[r]) != len(d[k - r]):
                return False

        return True
