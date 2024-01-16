from Node import *
from random import shuffle

def create_test_graph_directed(nodes_count, edges_count):
    """
    Creates an undirected graph with a specified number of nodes and edges.

    Parameters:
    nodes_count (int): Number of nodes in the graph.
    edges_count (int): Number of edges to be added in the graph.

    Returns:
    list: A list of Node objects representing the graph.

    The function ensures that there are no self-loops and each edge is bidirectional,
    i.e., if there is an edge from node A to B, there is also an edge from B to A.
    """
    vertices = [Node(i) for i in range(nodes_count)]

    all_edges = [[i, j] for i in range(nodes_count) for j in range(i + 1, nodes_count)]

    shuffle(all_edges)

    for i in range(min(edges_count, len(all_edges))):
        edge = all_edges[i]
        vertices[edge[0]].friends.append(vertices[edge[1]])
        vertices[edge[1]].friends.append(vertices[edge[0]])

    return vertices

def print_graph(vertices):
    """
    Prints a representation of the graph.

    Parameters:
    vertices (list): A list of Node objects representing the graph.
    """
    for n in vertices:
        print(str(n.data), end=": {")
        for t in n.friends:
            print(str(t.data), end=" ")
        print()

def print_graph_rec(root, visited_nodes):
    """
    Helper function to recursively print the graph.

    Parameters:
    root (Node): The node to start printing from.
    visited_nodes (set): A set to keep track of visited nodes.

    This function is used to print the graph starting from a specific node.
    It ensures that each node is printed exactly once.
    """
    if root is None or root in visited_nodes:
        return

    visited_nodes.add(root)

    print(str(root.data), end=": {")
    for n in root.friends:
        print(str(n.data), end=" ")
    print("}")

    for n in root.friends:
        print_graph_rec(n, visited_nodes)

def print_graph(root):
    """
    Prints the graph starting from a given root node.
    It ensures each node in the graph is printed only once.

    Parameters:
    root (Node): The starting node for printing the graph.

    The function initializes an empty set to track visited nodes and
    calls a recursive helper function to print the graph.
    """
    visited_nodes = set()
    print_graph_rec(root, visited_nodes)
