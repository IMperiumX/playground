from abc import ABC, abstractmethod


class HeapADT(ABC):
    """
    A class representing a Heap data structure.
    """

    @abstractmethod
    def insert(self, value):
        pass

    @abstractmethod
    def extract_min(self):
        pass

    @abstractmethod
    def _heapify_up(self):
        pass

    @abstractmethod
    def _heapify_down(self):
        pass
