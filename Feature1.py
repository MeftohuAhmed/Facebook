import numpy as np


def DFS(friends, n, visited, v):
    """
    Perform a Depth-First Search (DFS) to find all members of a friend circle.

    Args:
    friends (np.array): A 2D numpy array representing the friendship relationships.
    n (int): The number of users in the network.
    visited (np.array): An array keeping track of visited users.
    v (int): The current user index being explored.

    Returns:
    None: This function modifies the visited array in-place.
    """
    for x in range(n):
        # Check if there is a friendship and the user has not been visited
        if friends[v, x] and visited[x] == 0:
            # Mark as visited and continue the search
            if x != v:
                visited[x] = 1
                DFS(friends, n, visited, x)


def friend_circles(friends, n):
    """
    Find the number of friend circles in a given friendship network.

    Args:
    friends (np.array): A 2D numpy array representing the friendship relationships.
    n (int): The number of users in the network.

    Returns:
    int: The number of friend circles in the network.
    """
    if n == 0:
        return 0

    num_circles = 0  # Initialize the count of friend circles
    visited = np.zeros((n))  # Array to keep track of visited users

    for i in range(n):
        # If user i is not in any circle, find all friends in their circle
        if visited[i] == 0:
            visited[i] = 1
            DFS(friends, n, visited, i)
            num_circles += 1

    return num_circles


# Test cases
if __name__ == "__main__":
    # Test case 1: Two distinct friend circles within a group of four
    n1 = 4
    friends1 = np.array([
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 1]
    ])
    print("Number of friend circles in Test Case 1:", friend_circles(friends1, n1))  # Expected output: 2

    # Test case 2: No friends
    n2 = 3
    friends2 = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])
    print("Number of friend circles in Test Case 2:", friend_circles(friends2, n2))  # Expected output: 3

    # Test case 3: All are friends with each other
    n3 = 3
    friends3 = np.array([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ])
    print("Number of friend circles in Test Case 3:", friend_circles(friends3, n3))  # Expected output: 1


