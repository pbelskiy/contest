def get_cheapest_cost(rootNode):

  def dfs(node, total):
    if not node:
      return 0

    best = float('inf')
    for child in rootNode.children:
      best = min(best, total + rootNode.val + dfs(child))

    return best

  return dfs(rootNode, 0)


##########################################
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node
class Node:

  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None
