def moveZerosToEnd(arr):
    # Third solution
    # TC: O(N)
    # SC: O(1)

    # [1,1,1,1,1,1,1,1,1,1] => O(N)
    # [0,1,0,1,0,1,0,1,0,1]
    # [1,0,.... => last = 1


    # 1 2 3 0 0 0 0 0 0 0 4 5 6
    #       |             |
    # 1 2 3 4 0 0 0 0 0 0 0 5 6
    #         |           |
    #                     last
    last = None
    for i in range(len(arr)):
        if arr[i] != 0:
            continue

        if last is None:
            last = i + 1

        # found a zero, then swap with non zero
        for j in range(last, len(arr)):
            if arr[j] != 0:
                arr[i], arr[j] = arr[j], arr[i]
                last = j
                break

    return arr

    # First solution
    # TC: O(N) + O(N) => O(2N) => O(N)
    # SC: O(N)
    return list(filter(lambda n: n != 0, arr)) + [0]*arr.count(0)

    # Second solution
    # TC: O(N*2)
    # SC: O(1) -- because of inplace swap
    for i in range(len(arr)):
        if arr[i] != 0:
            continue

        # found a zero, then swap with non zero
        for j in range(i + 1, len(arr)):
            if arr[j] != 0:
                arr[i], arr[j] = arr[j], arr[i]
                break

    # [1, 0, 0, 0, 0, 0 ,0, 1]
    # -> [1, 1, 0, 0, 0, 0 ,0, 0]
    return arr
