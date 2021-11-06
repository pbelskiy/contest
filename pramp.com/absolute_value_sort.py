def absSort(arr):
    arr.sort(cmp=lambda a, b: a - b if abs(a) == abs(b) else abs(a) - abs(b))
    return arr
