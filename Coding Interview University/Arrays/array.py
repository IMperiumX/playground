import array
import ctypes
import math


class Vector:
    def __init__(self, initial_capacity=16, element_type="i"):  # 'i' for signed int
        # if starting number is greater, use power of 2 - 16, 32, 64, 128
        self._capacity = (
            2 ** round(math.log2(initial_capacity))
            if initial_capacity > 16
            else initial_capacity
        )
        self._size = 0
        self._data = array.array(element_type, [0] * self._capacity)

    def size(self):
        """Number of elements it contains"""
        return len(self)

    def capacity(self):
        """Number of elements it can hold without resizing"""
        return self._capacity

    def is_empty(self):
        """Check if the vector is empty"""
        return bool(len(self))

    def at(self, index):
        return self.__getitem__(index)

    def push(self, item):
        if self.is_full:
            self._resize(2 * self._capacity)
        self._data[self._size] = item
        self._size += 1

    def insert(self, index, item):
        if not 0 <= index <= self._size:  # Allow insertion at the end
            raise IndexError("Index out of bounds")
        if self.is_full:
            self._resize(2 * self._capacity)
        for i in range(self._size, index, -1):  # Shift elements to the right
            self._data[i] = self._data[i - 1]
        self._data[index] = item
        self._size += 1

    def prepend(self, item):
        self.insert(0, item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty vector")
        self._size -= 1
        value = self._data[self._size]
        if (
            self._size <= self._capacity // 4 and self._capacity > 16
        ):  # Don't shrink below 16
            self._resize(self._capacity // 2)
        return value

    def _remove(self, index):
        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds")
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._size -= 1
        if (
            self._size <= self._capacity // 4 and self._capacity > 16
        ):  # Don't shrink below 16
            self._resize(self._capacity // 2)

    def remove(self, item):
        for i in range(self._size):
            if self._data[i] == item:
                self._remove(i)
                # return  # Only removes the first occurrence

    def find(self, item):
        for i in range(self._size):
            if self._data[i] == item:
                return i
        return -1

    def _resize(self, new_capacity):
        new_data = array.array(self._data.typecode, [0] * new_capacity)
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def __getitem__(self, index):
        """Access element at index"""
        if not 0 <= index < self._size:
            raise IndexError(
                f"Given index: {index} is larger than \
                    array size {self.size}",
            )
        return self._data[index]  # Direct indexing into the array

    @property
    def is_full(self):
        return self._size == self._capacity

    def __len__(self):
        return self._size

    def __str__(self):
        return str(self._data[: self._size])

    def __repr__(self):
        return str(self._data[: self._size])

    def __iter__(self):
        return iter(self._data[: self._size])

    def __contains__(self, item):
        return item in self._data[: self._size]

    def __reversed__(self):
        return reversed(self._data[: self._size])

    def __add__(self, other):
        return self._data[: self._size] + other

    def __radd__(self, other):
        return other + self._data[: self._size]

    def __iadd__(self, other):
        self._data[: self._size] += other
        return self


class DynamicArray:
    """
    Dynamic Array implementation similar to Python's list.

    Attributes:
        _n (int): The number of elements currently stored in the array.
        _capacity (int): The current capacity of the array.
        _A (ctypes.py_object array): The underlying array used for storage.
        _SHRINK_THRESHOLD (float): The threshold (load factor) at which to shrink the array.
        _RESIZE_FACTOR (float): The factor by which to grow the array when resizing.
    """

    _SHRINK_THRESHOLD = 0.25  # Shrink when the array is 25% full
    _RESIZE_FACTOR = 2.0  # Double the capacity when resizing

    def __init__(self, initial_capacity=10, resize_factor=2.0):
        """
        Initializes the DynamicArray.

        Args:
            initial_capacity (int): The initial capacity of the array. Must be > 0.
            resize_factor (float): The factor by which to grow the array on resize. Must be > 1.
        """

        if not isinstance(initial_capacity, int) or initial_capacity <= 0:
            raise ValueError("Initial capacity must be a positive integer.")
        if not isinstance(resize_factor, (int, float)) or resize_factor <= 1.0:
            raise ValueError("Resize factor must be a number greater than 1.")

        self._n = 0
        self._capacity = initial_capacity
        self._A = self._make_array(self._capacity)
        self._RESIZE_FACTOR = float(resize_factor)  # Ensure it's a float

    def __len__(self):
        """
        Returns the number of elements in the array.

        Returns:
            int: The number of elements.
        """
        return self._n

    def __getitem__(self, index):
        """
        Retrieves the element at the given index.

        Args:
            index (int): The index of the element to retrieve.

        Returns:
            object: The element at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        if not 0 <= index < self._n:
            raise IndexError("Index out of range.")
        return self._A[index]

    def __setitem__(self, index, obj):
        """
        Sets the element at the given index to the specified value.

        Args:
            index (int): The index to set.
            obj (object): The value to set at the index.

        Raises:
            IndexError: If the index is out of range.
        """
        if not 0 <= index < self._n:
            raise IndexError("Index out of range.")
        self._A[index] = obj

    def __iter__(self):
        """
        Returns an iterator for the array.

        Yields:
            object: The next element in the array.
        """
        for i in range(self._n):
            yield self._A[i]

    def __contains__(self, obj):
        """
        Checks if the array contains the specified object.

        Args:
            obj (object): The object to search for.

        Returns:
            bool: True if the object is found, False otherwise.
        """
        for i in range(self._n):
            if self._A[i] == obj:
                return True
        return False

    def __add__(self, other):
        """
        Concatenates this DynamicArray with another DynamicArray.

        Args:
            other (DynamicArray): The other DynamicArray to concatenate with.

        Returns:
            DynamicArray: A new DynamicArray containing all elements.

        Raises:
            TypeError: If 'other' is not a DynamicArray.
        """
        if not isinstance(other, DynamicArray):
            raise TypeError(
                "Can only concatenate DynamicArray with another DynamicArray."
            )

        result = DynamicArray(initial_capacity=self._n + other._n)
        for i in range(self._n):
            result.append(self._A[i])
        for i in range(other._n):
            result.append(other._A[i])
        return result

    def __repr__(self):
        """
        Returns a string representation of the array.

        Returns:
            str: A string representation of the array.
        """
        return f'[{", ".join(map(str, self))}]'

    def _make_array(self, c):
        """
        Creates a new ctypes array of the given capacity.

        Args:
            c (int): The capacity of the array.

        Returns:
            ctypes.py_object_Array_c: A new ctypes array.
        """
        if not isinstance(c, int) or c <= 0:
            raise ValueError("Capacity must be a positive integer.")
        return (ctypes.py_object * c)()

    def _resize(self, new_capacity):
        """
        Resizes the underlying array to the given capacity.

        Args:
            new_capacity (int): The new capacity of the array.
        """
        if not isinstance(new_capacity, int) or new_capacity <= 0:
            raise ValueError("New capacity must be a positive integer.")

        B = self._make_array(new_capacity)
        for i in range(self._n):
            B[i] = self._A[i]
        self._A = B
        self._capacity = new_capacity

    def append(self, obj):
        """
        Appends an element to the end of the array.

        Args:
            obj (object): The element to append.
        """
        if self._n == self._capacity:
            self._resize(int(self._capacity * self._RESIZE_FACTOR))
        self._A[self._n] = obj
        self._n += 1

    def insert(self, index, obj):
        """
        Inserts an element at the specified index.

        Args:
            index (int): The index at which to insert the element.
            obj (object): The element to insert.

        Raises:
            IndexError: If the index is out of range.
        """
        if not 0 <= index <= self._n:
            raise IndexError("Index out of range.")

        if self._n == self._capacity:
            self._resize(int(self._capacity * self._RESIZE_FACTOR))

        for j in range(self._n, index, -1):
            self._A[j] = self._A[j - 1]
        self._A[index] = obj
        self._n += 1

    def pop(self, index=-1):
        """
        Removes and returns the element at the given index (default: last element).

        Args:
            index (int): The index of the element to remove.

        Returns:
            object: The removed element.

        Raises:
            IndexError: If the index is out of range or the array is empty.
        """
        if not 0 <= index < self._n:
            if index == -1 and self._n > 0:
                index = self._n - 1
            else:
                raise IndexError("Index out of range.")

        value = self._A[index]

        for j in range(index, self._n - 1):
            self._A[j] = self._A[j + 1]

        self._A[self._n - 1] = None  # Help garbage collection
        self._n -= 1

        # Shrink the array if it's less than _SHRINK_THRESHOLD full
        if (
            self._n < int(self._capacity * self._SHRINK_THRESHOLD)
            and self._capacity > 1
        ):
            self._resize(max(int(self._capacity / self._RESIZE_FACTOR), 1))

        return value

    def remove(self, obj):
        """
        Removes the first occurrence of the specified element from the array.

        Args:
            obj (object): The element to remove.

        Raises:
            ValueError: If the element is not found in the array.
        """
        for i in range(self._n):
            if self._A[i] == obj:
                self.pop(i)
                return
        raise ValueError("Element not found in array.")

    def extend(self, iterable):
        """
        Extends the array by appending elements from an iterable.

        Args:
            iterable (iterable): The iterable containing elements to append.
        """
        for item in iterable:
            self.append(item)

    def clear(self):
        """
        Removes all elements from the array.
        """
        self._n = 0
        self._A = self._make_array(self._capacity)  # Reset to initial capacity


if __name__ == "__main__":
    # Create a DynamicArray with initial capacity 5 and resize factor 1.5
    my_array = DynamicArray(initial_capacity=5, resize_factor=1.5)

    # Append elements
    my_array.append(10)
    my_array.append(20)
    my_array.append(30)

    print(len(my_array))  # Output: 3
    print(my_array)  # Output: [10, 20, 30]

    # Insert an element
    my_array.insert(1, 15)
    print(my_array)  # Output: [10, 15, 20, 30]

    # Access an element
    print(my_array[2])  # Output: 20

    # Remove an element
    my_array.remove(15)
    print(my_array)  # Output: [10, 20, 30]

    # Pop an element
    popped_value = my_array.pop()
    print(popped_value)  # Output: 30
    print(my_array)  # Output: [10, 20]

    # Extend with another DynamicArray
    other_array = DynamicArray()
    other_array.extend([40, 50])
    my_array.extend(other_array)
    print(my_array)  # Output: [10, 20, 40, 50]

    # Concatenate using + operator
    new_array = my_array + other_array
    print(new_array)  # Output: [10, 20, 40, 50, 40, 50]

    # Check for element existence
    print(20 in my_array)  # Output: True
    print(60 in my_array)  # Output: False

    # Clear the array
    my_array.clear()
    print(len(my_array))  # Output: 0
    print(my_array)  # Output: []
