class Node:
    """
  A class representing a node in a graph.

  Each node has data and a list of friends (adjacent nodes).
  """

    def __init__(self, data):
        """
    Initializes a new graph Node.

    Args:
        data: The data associated with the node.
    """
        self.data = data
        self.friends = []