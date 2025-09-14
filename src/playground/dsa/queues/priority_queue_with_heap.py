from playground.dsa import Heap, HeapADT


class PriorityQueue:
    """priority queue with heap"""

    def __init__(self):
        self.heap: HeapADT = Heap()

    def enqueue(self, item):
        self.heap.insert(item)

    def dequeue(self):
        return self.heap.extract_min()
