def get_indices_of_item_wights(arr, limit):
  d = {}

  for i, n in enumerate(arr):
    rest = limit - n
    if rest in d:
      return [i, d[rest]]

    d[n] = i

  return []
