# TODO: Why this not working (comp (j, j+1) not this comparision)
def inefficient_bubble_sort(arr):
    for j, left in enumerate(arr):
        for i, right in enumerate(arr):
            if right > left:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


def bubble_sort(list):
    n = len(list)

    for i in range(n - 1):
        for j in range(n - 1):
            if list[j] > list[j + 1]:
                tmp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = tmp

    return list


def bubble_sort_iterative(collection):
    length = len(collection)
    # reversed(range(length)) same as range(n-1, -1, -1)
    # diff between starting from largest index to smallest index
    for i in reversed(range(length)):
        swapped = False  # `swapped` flag to check if the original collection is already sorted (one iteration is enough)
        for j in range(i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break  # Stop iteration if the collection is sorted.
    return collection


def bubble_sort_recursive(collection):
    length = len(collection)
    swapped = False
    for i in range(length - 1):
        if collection[i] > collection[i + 1]:
            collection[i], collection[i + 1] = collection[i + 1], collection[i]
            swapped = True

    return collection if not swapped else bubble_sort_recursive(collection)
