class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1]*n for _ in range(m)]

        y = -1
        x = -1

        while head:
            # right
            y += 1
            x += 1
            while x < n and head and mat[y][x] == -1:
                mat[y][x] = head.val
                head = head.next
                x += 1

            # down
            x -= 1
            y += 1
            while y < m and head and mat[y][x] == -1:
                mat[y][x] = head.val
                head = head.next
                y += 1

            # left
            y -= 1
            x -= 1
            while x >= 0 and head and mat[y][x] == -1:
                mat[y][x] = head.val
                head = head.next
                x -= 1

            # up
            y -= 1
            x += 1
            while y >= 0 and head and mat[y][x] == -1:
                mat[y][x] = head.val
                head = head.next
                y -= 1

        return mat
