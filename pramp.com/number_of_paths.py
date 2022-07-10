def num_of_paths_to_dest(n):

    def dfs(y, x):
        if (y, x) in memo:
            return memo[(y, x)]

        # diagonal
        if y > x:
            return 0

        # out of boundary
        if x > n or y > n:
            return 0

        if y == n - 1 and x == n - 1:
            return 1

        memo[(y, x)] = dfs(y + 1, x) + dfs(y, x + 1)
        return memo[(y, x)]

    memo = {}
    return dfs(0, 0)
