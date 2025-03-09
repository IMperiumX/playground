import timeit


def binary_search(a, k):
    """
    Binary search algorithm to find the index of the key in the list.
    :param a: List of elements
    :param k: Key to search
    :return: Index of the key if found, else -1
    """
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        guess = a[mid]
        if guess == k:
            return mid
        if k < guess:
            hi = mid - 1
        else:
            lo = mid + 1

    return -1


def binary_search_by_recursion(a, k, lo=0, hi=None):
    """
    Binary search algorithm to find the index of the key in the list.
    :param a: List of elements
    :param k: Key to search
    :param lo: Lower bound
    :param hi: Upper bound
    :return: Index of the key if found, else -1
    """
    if hi is None:
        hi = len(a) - 1
    if lo > hi:
        return -1
    mid = lo + (hi - lo) // 2
    guess = a[mid]
    if guess == k:
        return mid
    if k < guess:
        return binary_search_by_recursion(a, k, lo, mid - 1)
    return binary_search_by_recursion(a, k, mid + 1, hi)


searches = (
    binary_search,
    binary_search_by_recursion,
    # exponential_search # https://en.wikipedia.org/wiki/Exponential_search
)

if __name__ == "__main__":
    print("\nBenchmarks...")
    setup = "collection = range(10000)"
    for search in searches:
        name = search.__name__
        print(
            f"{name:>26}:",
            timeit.timeit(
                f"{name}(collection, 500)", setup=setup, number=5_000, globals=globals()
            ),
        )
        print("\n")
