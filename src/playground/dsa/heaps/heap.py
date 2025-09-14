from .heap_adt import HeapADT


class Heap(HeapADT):
    """
    A class representing a Min-Heap data structure.

    Attributes:
    -----------
    data : list
        A list to store heap elements.

    Methods:
    --------
    __init__(data=None):
        Initializes the heap with optional initial data.

    insert(value):
        Inserts a new value into the heap and maintains the heap property.

    _heapify_up():
        Maintains the heap property by moving the last element up to its correct position.

    extract_min():
        Removes and returns the minimum element from the heap.

    _heapify_down():
        Maintains the heap property by moving the root element down to its correct position.

    __str__():
        Returns a string representation of the heap.

    __len__():
        Returns the number of elements in the heap.

    __bool__():
        Returns True if the heap is not empty, False otherwise.

    __iter__():
        Returns an iterator for the heap elements.
    """

    def __init__(self, data=None):
        self.data = data or []

    def insert(self, value):
        self.data.append(value)
        self._heapify_up()

    def _heapifyqueues_up(self):
        index = len(self.data) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.data[index] < self.data[parent_index]:
                self.data[index], self.data[parent_index] = (
                    self.data[parent_index],
                    self.data[index],
                )
                index = parent_index
            else:
                break

    def extract_min(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()
        min_value = self.data[0]
        self.data[0] = self.data.pop()
        self._heapify_down()
        return min_value

    def _heapify_down(self):
        index = 0
        while index < len(self.data):
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            if left_child_index >= len(self.data):
                break
            if right_child_index >= len(self.data):
                min_child_index = left_child_index
            else:
                min_child_index = (
                    left_child_index
                    if self.data[left_child_index] < self.data[right_child_index]
                    else right_child_index
                )
            if self.data[index] > self.data[min_child_index]:
                self.data[index], self.data[min_child_index] = (
                    self.data[min_child_index],
                    self.data[index],
                )
                index = min_child_index
            else:
                break

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)

    def __bool__(self):
        return bool(self.data)

    def __iter__(self):
        return iter(self.data)


if __name__ == "__main__":
    h = Heap()
    h.insert(3)
    h.insert(2)
    h.insert(1)
    h.insert(15)
    h.insert(5)
    h.insert(4)
    h.insert(45)

    print(h.extract_min())
