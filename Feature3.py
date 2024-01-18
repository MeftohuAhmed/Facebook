def find_story_id(arr, key):
    """
    Perform a modified binary search on a rotated sorted array to find the index of a specified key.

    Parameters:
    arr (list of int): The rotated sorted array in which to search for the key.
    key (int): The value to search for within the array.

    Returns:
    int: The index of the key within the array. Returns -1 if the key is not found.
    """

    start = 0
    end = len(arr) - 1

    # Handle the case where the array is empty
    if start > end:
        return -1

    # Perform binary search
    while start <= end:
        mid = start + (end - start) // 2

        # Check if the key is found
        if arr[mid] == key:
            return mid

        # Determine the sorted half and adjust search range
        if arr[start] <= arr[mid] and key <= arr[mid] and key >= arr[start]:
            end = mid - 1
        elif arr[mid] <= arr[end] and key >= arr[mid] and key <= arr[end]:
            start = mid + 1
        elif arr[start] <= arr[mid] and arr[mid] <= arr[end] and key > arr[end]:
            start = mid + 1
        elif arr[end] <= arr[mid]:
            start = mid + 1
        elif arr[start] >= arr[mid]:
            end = mid - 1
        else:
            return -1

    return -1


# Test cases
v1 = [6, 7, 1, 2, 3, 4, 5]
print("Story(3) found at index: " + str(find_story_id(v1, 3)))
print("Story(6) found at index: " + str(find_story_id(v1, 6)))

v2 = [5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4]
print("Story(3) found at index: " + str(find_story_id(v2, 3)))
print("Story(6) found at index: " + str(find_story_id(v2, 6)))
