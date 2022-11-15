import collections


def shortestCellPath(grid, sr, sc, tr, tc):
  h, w = len(grid), len(grid[0])
  q = collections.deque([(sr, sc, 0)])
  v = set()

  while q:
    r, c, s = q.popleft()

    if r == tr and c == tc:
      return s

    for dr, dc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
      if not (0 <= dr < h and 0 <= dc < w):
        continue

      if grid[dr][dc] != 1:
        continue

      if (dr, dc) in v:
        continue

      v.add((dr, dc))
      q.append((dr, dc, s + 1))

  return -1

  # TC: O(h+w)
  # SC: O(h+w)
