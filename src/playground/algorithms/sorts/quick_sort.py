from random import randrange


def quick_sort_with_random_pivot(collection: list) -> list:
    # Base case: if the collection has 0 or 1 elements, it is already sorted
    if len(collection) < 2:
        return collection

    # Randomly select a pivot index and remove the pivot element from the collection
    pivot_index = randrange(len(collection))
    pivot = collection.pop(pivot_index)

    # Partition the remaining elements into two groups: lesser or equal, and greater
    lesser = [item for item in collection if item <= pivot]
    greater = [item for item in collection if item > pivot]

    # Recursively sort the lesser and greater groups, and combine with the pivot
    return [
        *quick_sort_with_random_pivot(lesser),
        pivot,
        *quick_sort_with_random_pivot(greater),
    ]


def quick_sort_with_first_pivot(collection: list) -> list:
    if len(collection) <= 1:
        return collection
    else:
        return [
            *quick_sort_with_first_pivot(
                [e for e in collection[1:] if e <= collection[0]]
            ),
            collection[0],
            *quick_sort_with_first_pivot(
                [e for e in collection[1:] if e > collection[0]]
            ),
        ]


if __name__ == "__main__":
    # Get user input and convert it into a list of integers
    # from random import sample

    # unsorted = sample(range(-5, 5), 10)
    unsorted = [29, 10, 14, 37, 14]

    # Print the result of sorting the user-provided list
    print(quick_sort_with_random_pivot(unsorted))
