def array_of_array_products(arr):
  # first idead was to use prefix sum (prodiuc),
  # TC: O(N)
  # SC: O(N)
  # we cannot solve it this way because of div prohibited
  total = 1
  for i in range(arr):
    total *= arr[i]

  res = []
  for i in range(arr):
    res.append(total // arr[i])

  return res

  # [2, 3, 4, 5]
  # prefix [1, 2, 6, 24]
  # postfix [60, 20, 5, 1]

  # 60, 40, 30, 24

  # Brute force
  # TC: O(N^2)
  # SC: O(N)
  res = []

  for i in range(arr):
    n = 1
    for j in range(arr):
      if i != j:
        n *= arr[i]
    res.append(n)

  return res
