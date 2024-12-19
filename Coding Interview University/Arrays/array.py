import array
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

