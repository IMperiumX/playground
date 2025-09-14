from abc import ABC, abstractmethod


class DynamicArrayADT(ABC):
    @abstractmethod
    def __init__(self, initial_capacity=10, resize_factor=2.0):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self, index):
        pass

    @abstractmethod
    def __setitem__(self, index, obj):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __contains__(self, obj):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def _make_array(self, c):
        pass
