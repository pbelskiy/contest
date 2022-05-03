class Solution:
    def alphabetBoardPath(self, target: str) -> str:

        def get_yx(char):
            v = ord(char) - ord('a')
            return v // 5, v % 5

        def get_path(a, b):
            y1, x1 = get_yx(a)
            y2, x2 = get_yx(b)

            dy = abs(y1 - y2)
            dx = abs(x1 - x2)

            path = ''

            if a == 'z':
                path += 'U'*dy if y1 > y2 else 'D'*dy
                path += 'L'*dx if x1 > x2 else 'R'*dx
            else:
                path += 'L'*dx if x1 > x2 else 'R'*dx
                path += 'U'*dy if y1 > y2 else 'D'*dy

            return path

        path = ''
        target = 'a' + target
        for a, b in zip(target, target[1:]):
            path += get_path(a, b) + '!'

        return path
