import unittest

from singly_linked_list import EmptyListError, LinkedList, Node, OutOfBoundsError


class TestLinkedList(unittest.TestCase):
    def test_empty_list(self):
        """Test operations on an empty list."""
        ll = LinkedList()
        self.assertTrue(ll.empty())
        self.assertEqual(ll.size(), 0)
        self.assertEqual(len(ll), 0)
        self.assertEqual(ll.front(), None)
        self.assertEqual(ll.back(), None)
        with self.assertRaises(EmptyListError):
            ll.pop_front()
        with self.assertRaises(EmptyListError):
            ll.pop_back()
        with self.assertRaises(OutOfBoundsError):
            ll.value_at(0)
        with self.assertRaises(OutOfBoundsError):
            ll.insert(1, 10)
        with self.assertRaises(OutOfBoundsError):
            ll.erase(0)

    def test_push_front(self):
        """Test adding elements to the front."""
        ll = LinkedList()
        ll.push_front(10)
        self.assertEqual(ll.size(), 1)
        self.assertEqual(ll.front(), 10)
        self.assertEqual(ll.back(), 10)
        ll.push_front(20)
        self.assertEqual(ll.size(), 2)
        self.assertEqual(ll.front(), 20)
        self.assertEqual(ll.back(), 10)

    def test_pop_front(self):
        """Test removing elements from the front."""
        ll = LinkedList()
        ll.push_front(10)
        ll.push_front(20)
        self.assertEqual(ll.pop_front(), 20)
        self.assertEqual(ll.size(), 1)
        self.assertEqual(ll.pop_front(), 10)
        self.assertEqual(ll.size(), 0)
        with self.assertRaises(EmptyListError):
            ll.pop_front()

    def test_push_back(self):
        """Test adding elements to the back."""
        ll = LinkedList()
        ll.push_back(10)
        self.assertEqual(ll.size(), 1)
        self.assertEqual(ll.front(), 10)
        self.assertEqual(ll.back(), 10)
        ll.push_back(20)
        self.assertEqual(ll.size(), 2)
        self.assertEqual(ll.front(), 10)
        self.assertEqual(ll.back(), 20)

    def test_pop_back(self):
        """Test removing elements from the back."""
        ll = LinkedList()
        ll.push_back(10)
        ll.push_back(20)
        self.assertEqual(ll.pop_back(), 20)
        self.assertEqual(ll.size(), 1)
        self.assertEqual(ll.pop_back(), 10)
        self.assertEqual(ll.size(), 0)
        with self.assertRaises(EmptyListError):
            ll.pop_back()

    def test_value_at(self):
        """Test accessing elements by index."""
        ll = LinkedList()
        ll.push_back(10)
        ll.push_back(20)
        ll.push_back(30)
        self.assertEqual(ll.value_at(0), 10)
        self.assertEqual(ll.value_at(1), 20)
        self.assertEqual(ll.value_at(2), 30)
        with self.assertRaises(OutOfBoundsError):
            ll.value_at(-1)
        with self.assertRaises(OutOfBoundsError):
            ll.value_at(3)

    def test_insert(self):
        """Test inserting elements at specific indices."""
        ll = LinkedList()
        ll.insert(0, 10)  # Insert at the beginning (empty list)
        self.assertEqual(ll.size(), 1)
        self.assertEqual(ll.value_at(0), 10)
        ll.insert(0, 5)  # Insert at the beginning
        self.assertEqual(ll.size(), 2)
        self.assertEqual(ll.value_at(0), 5)
        self.assertEqual(ll.value_at(1), 10)
        ll.insert(1, 7)  # Insert in the middle
        self.assertEqual(ll.size(), 3)
        self.assertEqual(ll.value_at(0), 5)
        self.assertEqual(ll.value_at(1), 7)
        self.assertEqual(ll.value_at(2), 10)
        ll.insert(3, 15)  # Insert at end
        self.assertEqual(ll.size(), 4)
        self.assertEqual(ll.value_at(0), 5)
        self.assertEqual(ll.value_at(1), 7)
        self.assertEqual(ll.value_at(2), 10)
        self.assertEqual(ll.value_at(3), 15)
        with self.assertRaises(OutOfBoundsError):
            ll.insert(-1, 20)
        with self.assertRaises(OutOfBoundsError):
            ll.insert(5, 25)

    def test_erase(self):
        """Test removing elements at specific indices."""
        ll = LinkedList()
        ll.push_back(10)
        ll.push_back(20)
        ll.push_back(30)
        ll.erase(1)  # Erase from the middle
        self.assertEqual(ll.size(), 2)
        self.assertEqual(ll.value_at(0), 10)
        self.assertEqual(ll.value_at(1), 30)
        ll.erase(0)  # Erase from the beginning
        self.assertEqual(ll.size(), 1)
        self.assertEqual(ll.value_at(0), 30)
        ll.erase(0)  # Erase the last element
        self.assertEqual(ll.size(), 0)
        with self.assertRaises(OutOfBoundsError):
            ll.erase(0)
        with self.assertRaises(OutOfBoundsError):
            ll.erase(-1)

    def test_value_n_from_end(self):
        """Test getting the value n elements from the end."""
        ll = LinkedList()
        ll.push_back(10)
        ll.push_back(20)
        ll.push_back(30)
        ll.push_back(40)
        ll.push_back(50)
        self.assertEqual(ll.value_n_from_end(1), 50)
        self.assertEqual(ll.value_n_from_end(3), 30)
        self.assertEqual(ll.value_n_from_end(5), 10)
        with self.assertRaises(ValueError):
            ll.value_n_from_end(0)  # n must be positive
        with self.assertRaises(ValueError):
            ll.value_n_from_end(-2)  # n must be positive
        with self.assertRaises(OutOfBoundsError):
            ll.value_n_from_end(6)  # n greater than list size

    def test_reverse(self):
        """Test reversing the list."""
        ll = LinkedList()
        ll.push_back(10)
        ll.push_back(20)
        ll.push_back(30)
        ll.reverse()
        self.assertEqual(ll.value_at(0), 30)
        self.assertEqual(ll.value_at(1), 20)
        self.assertEqual(ll.value_at(2), 10)
        ll.reverse()  # Reverse back
        self.assertEqual(ll.value_at(0), 10)
        self.assertEqual(ll.value_at(1), 20)
        self.assertEqual(ll.value_at(2), 30)

        # Test reversing a list with one element
        ll_single = LinkedList()
        ll_single.push_back(5)
        ll_single.reverse()
        self.assertEqual(ll_single.value_at(0), 5)

        # Test reversing an empty list
        ll_empty = LinkedList()
        ll_empty.reverse()
        self.assertTrue(ll_empty.empty())

    def test_remove_value(self):
        """Test removing the first occurrence of a value."""
        ll = LinkedList()
        ll.push_back(10)
        ll.push_back(20)
        ll.push_back(30)
        ll.push_back(20)
        ll.remove_value(20)
        self.assertEqual(ll.size(), 3)
        self.assertEqual(ll.value_at(0), 10)
        self.assertEqual(ll.value_at(1), 30)
        self.assertEqual(ll.value_at(2), 20)
        ll.remove_value(10)  # Remove from the beginning
        self.assertEqual(ll.size(), 2)
        self.assertEqual(ll.value_at(0), 30)
        self.assertEqual(ll.value_at(1), 20)
        ll.remove_value(20)  # Remove from the end
        self.assertEqual(ll.size(), 1)
        self.assertEqual(ll.value_at(0), 30)
        ll.remove_value(30)  # Remove the last element
        self.assertEqual(ll.size(), 0)
        ll.remove_value(
            40
        )  # Try to remove a non-existent value (shouldn't do anything)
        self.assertEqual(ll.size(), 0)

    def test_iterator(self):
        """Test the iterator."""
        ll = LinkedList()
        ll.push_back(1)
        ll.push_back(2)
        ll.push_back(3)

        # Test using a for loop
        items = []
        for item in ll:
            items.append(item)
        self.assertEqual(items, [1, 2, 3])

        # Test using list comprehension
        items = [item for item in ll]
        self.assertEqual(items, [1, 2, 3])

        # Test manual iteration using next()
        it = iter(ll)
        self.assertEqual(next(it), 1)
        self.assertEqual(next(it), 2)
        self.assertEqual(next(it), 3)
        with self.assertRaises(StopIteration):
            next(it)

    def test_repr(self):
        """Test the __repr__ method."""
        ll = LinkedList()
        self.assertEqual(repr(ll), "")

        ll.push_back(1)
        self.assertEqual(repr(ll), "1")

        ll.push_back(2)
        ll.push_back(3)
        self.assertEqual(repr(ll), "1 => 2 => 3")

    def test_init_with_non_empty_list(self):
        """Test the __init__ method when passing a non-empty linked list."""
        # Create an initial linked list manually using Node objects
        node3 = Node(3)
        node2 = Node(2, node3)
        node1 = Node(1, node2)

        # Initialize a new LinkedList with the head of the manually created list
        ll = LinkedList(head=node1)

        # Check if the new linked list is constructed correctly
        self.assertEqual(ll.size(), 3)
        self.assertEqual(ll.value_at(0), 1)
        self.assertEqual(ll.value_at(1), 2)
        self.assertEqual(ll.value_at(2), 3)


if __name__ == "__main__":
    unittest.main()
