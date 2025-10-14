from typing import Any


def bubble_sort_iterative(collection: list[Any]) -> list[Any]:
    length = len(collection)
    for i in reversed(range(length)):
        swapped = False
        for j in range(i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break  # Stop iteration if the collection is sorted.
    return collection


def bubble_sort_recursive(collection: list[Any]) -> list[Any]:
    length = len(collection)
    swapped = False
    for i in range(length - 1):
        if collection[i] > collection[i + 1]:
            collection[i], collection[i + 1] = collection[i + 1], collection[i]
            swapped = True

    return collection if not swapped else bubble_sort_recursive(collection)


if __name__ == "__main__":
    from random import sample

    # doctest.testmod()

    # Benchmark: Iterative seems slightly faster than recursive.
    unsorted = sample(range(-5, 5), 10)
    print("\nIterative bubble sort:")
    print(*bubble_sort_iterative(unsorted), sep=",")

    unsorted = sample(range(-5, 5), 10)
    print("\nRecursive bubble sort:")
    print(*bubble_sort_recursive(unsorted), sep=",")
