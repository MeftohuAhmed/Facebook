from CloneGraph import *


def clone_recursive(root, nodes_completed):
    """
    Recursively clone a directed graph starting from the given root node.

    Args:
    root: The root node of the graph to be cloned.
    nodes_completed: A dictionary to keep track of nodes that have been cloned.

    Returns:
    The cloned root node of the graph.
    """
    if root is None:
        return None

    new_node = Node(root.data)
    nodes_completed[root] = new_node

    for p in root.friends:
        x = nodes_completed.get(p)
        if x is None:
            new_node.friends.append(clone_recursive(p, nodes_completed))
        else:
            new_node.friends.append(x)

    return new_node


def clone_graph(root):
    """
    Clone a directed graph.

    Args:
    root: The root node of the graph to be cloned.

    Returns:
    The cloned root node of the graph.
    """
    nodes_completed = {}
    return clone_recursive(root, nodes_completed)


if __name__ == "__main__":
    # Create a directed graph with 7 vertices and 18 edges
    vertices = create_test_graph_directed(7, 18)  # Assuming you have a function to create the graph

    # Print the original graph
    print("Original Graph:")
    print_graph(vertices[0])  # Assuming you have a function to print the graph

    # Clone the graph
    cp = clone_graph(vertices[0])

    # Print the cloned graph
    print("\nAfter Copy:")
    print_graph(cp)  # Assuming you have a function to print the cloned graph