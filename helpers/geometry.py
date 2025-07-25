def is_point_between(a, b, p):
    # vectors
    ab = [b[0] - a[0], b[1] - a[1]]
    ap = [p[0] - a[0], p[1] - a[1]]

    # check collinearity
    cross = ab[0] * ap[1] - ab[1] * ap[0]
    if cross != 0:
        return False

    # check p inside rectangle
    min_x, max_x = min(a[0], b[0]), max(a[0], b[0])
    min_y, max_y = min(a[1], b[1]), max(a[1], b[1])

    return min_x <= p[0] <= max_x and min_y <= p[1] <= max_y
