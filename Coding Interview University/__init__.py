def mergesort(array):
    """Sorts the given array using mergesort."""
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_half = mergesort(array[:mid])
    right_half = mergesort(array[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    """Merges two sorted arrays into a single sorted array."""
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

def quicksort(array):
    """Sorts the given array using quicksort."""
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def selection_sort(array):
    """Sorts the given array using selection sort."""
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

def insertion_sort(array):
    """Sorts the given array using insertion sort."""
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

# Example usage
array = [5, 3, 8, 1, 4]
print("Mergesort:", mergesort(array[:]))
print("Quicksort:", quicksort(array[:]))
print("Selection sort:", selection_sort(array[:]))
print("Insertion sort:", insertion_sort(array[:]))
