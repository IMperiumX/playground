import unittest
from playground.dsa.arrays import DynamicArray


class TestDynamicArray(unittest.TestCase):
    def test_initialization(self):
        """Test initialization of DynamicArray."""
        da = DynamicArray()
        self.assertEqual(len(da), 0)
        self.assertEqual(da._capacity, 10)

        da_custom = DynamicArray(initial_capacity=5, resize_factor=1.5)
        self.assertEqual(len(da_custom), 0)
        self.assertEqual(da_custom._capacity, 5)
        self.assertEqual(da_custom._RESIZE_FACTOR, 1.5)

        with self.assertRaises(ValueError):
            DynamicArray(initial_capacity=-1)
        with self.assertRaises(ValueError):
            DynamicArray(resize_factor=1.0)

    def test_append(self):
        """Test appending elements to DynamicArray."""
        da = DynamicArray(initial_capacity=2)
        da.append(1)
        da.append(2)
        self.assertEqual(len(da), 2)
        self.assertEqual(da[0], 1)
        self.assertEqual(da[1], 2)

        da.append(3)
        self.assertEqual(len(da), 3)
        self.assertEqual(da[2], 3)
        self.assertEqual(da._capacity, 4)  # Capacity should have doubled

    def test_insert(self):
        """Test inserting elements into DynamicArray."""
        da = DynamicArray()
        da.append(1)
        da.append(3)
        da.insert(1, 2)
        self.assertEqual(len(da), 3)
        self.assertEqual(da[0], 1)
        self.assertEqual(da[1], 2)
        self.assertEqual(da[2], 3)

        with self.assertRaises(IndexError):
            da.insert(5, 4)

    def test_pop(self):
        """Test popping elements from DynamicArray."""
        da = DynamicArray()
        da.append(1)
        da.append(2)
        da.append(3)
        self.assertEqual(da.pop(), 3)
        self.assertEqual(len(da), 2)
        self.assertEqual(da.pop(0), 1)
        self.assertEqual(len(da), 1)

        with self.assertRaises(IndexError):
            da.pop(5)

    def test_remove(self):
        """Test removing elements from DynamicArray."""
        da = DynamicArray()
        da.append(1)
        da.append(2)
        da.append(3)
        da.remove(2)
        self.assertEqual(len(da), 2)
        self.assertNotIn(2, da)

        with self.assertRaises(ValueError):
            da.remove(4)

    def test_extend(self):
        """Test extending DynamicArray with an iterable."""
        da = DynamicArray()
        da.extend([1, 2, 3])
        self.assertEqual(len(da), 3)
        self.assertEqual(da[0], 1)
        self.assertEqual(da[1], 2)
        self.assertEqual(da[2], 3)

    def test_clear(self):
        """Test clearing DynamicArray."""
        da = DynamicArray()
        da.append(1)
        da.append(2)
        da.clear()
        self.assertEqual(len(da), 0)

    def test_contains(self):
        """Test checking if an element exists in DynamicArray."""
        da = DynamicArray()
        da.append(1)
        da.append(2)
        self.assertTrue(1 in da)
        self.assertFalse(3 in da)

    def test_add(self):
        """Test concatenating two DynamicArrays."""
        da1 = DynamicArray()
        da1.append(1)
        da1.append(2)
        da2 = DynamicArray()
        da2.append(3)
        da2.append(4)
        da3 = da1 + da2
        self.assertEqual(len(da3), 4)
        self.assertEqual(da3[0], 1)
        self.assertEqual(da3[1], 2)
        self.assertEqual(da3[2], 3)
        self.assertEqual(da3[3], 4)

        with self.assertRaises(TypeError):
            da1 + [5, 6]

    def test_repr(self):
        """Test string representation of DynamicArray."""
        da = DynamicArray()
        self.assertEqual(repr(da), "[]")
        da.append(1)
        da.append(2)
        self.assertEqual(repr(da), "[1, 2]")


if __name__ == "__main__":
    unittest.main()
