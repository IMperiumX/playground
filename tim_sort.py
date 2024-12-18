def timsort(array):
    """Sorts an array using the Timsort algorithm.

    Args:
            array: The array to be sorted.

    Returns:
            The sorted array (in-place).
    """

    MIN_RUN = 32  # Minimum run size, often a power of 2

    def insertion_sort(array, left, right):
        """Performs insertion sort on a subarray.

        Args:
                array: The array to be sorted.
                left: The starting index of the subarray.
                right: The ending index of the subarray.
        """

        for i in range(left + 1, right + 1):
            key = array[i]
            j = i - 1
            while j >= left and array[j] > key:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key

    def merge(array, left, mid, right):
        """Merges two sorted subarrays.

        Args:
                array: The array containing the subarrays.
                left: The starting index of the left subarray.
                mid: The ending index of the left subarray.
                right: The ending index of the right subarray.
        """

        # Optimization: Use slices instead of pop for faster merging
        left_array = array[left : mid + 1]
        right_array = array[mid + 1 : right + 1]
        i = j = 0
        k = left

        while i < len(left_array) and j < len(right_array):
            if left_array[i] <= right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        # Copy any remaining elements
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1
        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1

    n = len(array)

    # Create and sort initial runs
    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN, n)
        insertion_sort(array, start, end - 1)

    # Merge runs until the array is sorted
    size = MIN_RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min(n - 1, left + 2 * size - 1)
            if mid < right:  # Ensure there are two runs to merge
                merge(array, left, mid, right)
        size *= 2

    return array


def timsort2(the_array):
    MIN_MERGE = 32  # Minimum run size

    def calc_min_run(n):
        r = 0
        while n >= MIN_MERGE:
            r |= n & 1  # Keep track of whether n is odd
            n >>= 1  # Right shift n by 1
        return n + r  # Return the adjusted run length

    def insertion_sort(the_array, left, right):
        # Sort a portion of the array using insertion sort
        for i in range(left + 1, right + 1):
            key = the_array[i]
            j = i - 1
            while j >= left and the_array[j] > key:
                the_array[j + 1] = the_array[j]  # Shift element to the right
                j -= 1
            the_array[j + 1] = key  # Place key at its correct position

    def merge(the_array, left, mid, right):
        # Merge two sorted halves
        len1, len2 = mid - left + 1, right - mid
        left_array = the_array[left : mid + 1]
        right_array = the_array[mid + 1 : right + 1]
        i, j, k = 0, 0, left

        # Merging process
        while i < len1 and j < len2:
            if left_array[i] <= right_array[j]:
                the_array[k] = left_array[i]
                i += 1
            else:
                the_array[k] = right_array[j]
                j += 1
            k += 1

        # Copying remaining elements of left_array if any
        while i < len1:
            the_array[k] = left_array[i]
            k += 1
            i += 1

        # Copying remaining elements of right_array if any
        while j < len2:
            the_array[k] = right_array[j]
            k += 1
            j += 1

    n = len(the_array)  # Length of the array
    min_run = calc_min_run(n)  # Calculate minimum run length

    # Step 1: Sort individual runs using insertion sort
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(the_array, start, end)

    # Step 2: Start merging from size min_run (or 32). It will merge to the whole array.
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)  # Midpoint of the current run
            right = min((left + 2 * size - 1), (n - 1))  # End of the second run
            if mid < right:  # Ensure there are elements to merge
                merge(the_array, left, mid, right)
        size *= 2  # Double the size for the next merge

    return the_array  # Return the sorted array
