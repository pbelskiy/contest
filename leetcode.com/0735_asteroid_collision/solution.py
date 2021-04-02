#!/usr/bin/env python3

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        q = []

        for a in asteroids:
            if a < 0 and (len(q) == 0 or q[-1] < 0):
                q.append(a)
                continue

            elif a > 0:
                q.append(a)
                continue

            add = True
            while len(q) > 0:
                if q[-1] < 0:
                    break

                if abs(q[-1]) < abs(a):
                    q.pop()
                    continue

                if abs(q[-1]) > abs(a):
                    add = False
                    break

                if abs(q[-1]) == abs(a):
                    q.pop()
                    add = False
                    break

            if add:
                q.append(a)

        return q
