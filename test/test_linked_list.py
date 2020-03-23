from io import StringIO
import sys
import unittest
from linked_list import Node, LinkedList, DoublyNode, DoublyLinkedList

class LinkedListTests(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()
        self.helper = SharedListTestHelpers()

    def tearDown(self):
        pass

    def test_add_first_no_head(self):
        self.helper.helper_add_first_no_head(self.linked_list, Node(5))

    def test_add_first_has_head(self):
        old_head = Node(7)
        new_head = Node(30)

        self.helper.helper_add_first_has_head(self.linked_list, old_head, new_head)

    def test_add_last_no_head(self):
        self.helper.helper_add_last_no_head(self.linked_list, Node(9))

    def test_add_last_has_head(self):
        second_to_last = Node(55)
        last_node = Node(7)

        self.helper.helper_add_last_has_head(self.linked_list, second_to_last, last_node)

    def test_add_last_in_list(self):
        head = Node(123)
        to_be_last_node = Node(555)

        head.next = to_be_last_node
        to_be_last_node.next = Node(7656)

        self.linked_list.head = head
        self.helper.helper_add_last_in_list(self.linked_list, to_be_last_node)

    def test_print_list_empty(self):
        self.helper.helper_print_list_empty(self.linked_list)

    def test_insert_after_no_head(self):
        self.helper.helper_insert_after_no_head(self.linked_list, Node(7))

    def test_insert_after_only_head(self):
        prev_node = Node(1)
        new_node = Node(11)

        self.helper.helper_insert_after_only_head(self.linked_list, prev_node, new_node)

    def test_insert_after_after_head(self):
        prev_node = Node(2)
        new_node = Node(5)

        self.linked_list.head = Node(7)
        self.linked_list.head.next = prev_node

        self.helper.helper_insert_after_after_head(self.linked_list, prev_node, new_node)

    def test_insert_before_no_head(self):
        after_node = Node(2)
        new_node = Node(1000)

        self.helper.helper_insert_before_no_head(self.linked_list, after_node, new_node)

    def test_insert_before_only_head(self):
        after_node = Node(99999)
        new_node = Node(1246)

        self.helper.helper_insert_before_only_head(self.linked_list, after_node, new_node)

    def test_insert_before_after_head(self):
        after_node = Node(765)
        new_node = Node(123)

        self.linked_list.head = Node(3)
        self.linked_list.head.next = after_node

        self.helper.helper_insert_before_after_head(self.linked_list, after_node, new_node)

    def test_delete_node_no_head(self):
        self.helper.helper_delete_node_no_head(self.linked_list, 900)

    def test_delete_node_only_head(self):
        node_to_delete = Node(6)
        self.helper.helper_delete_node_only_head(self.linked_list, node_to_delete)

    def test_delete_node_after_head(self):
        head = Node(6)
        after_node = Node(100)
        node_to_delete = Node(8528)

        head.next = node_to_delete
        node_to_delete.next = after_node

        self.helper.helper_delete_node_after_head(self.linked_list, head, node_to_delete)

    def test_clone_no_head(self):
        self.helper.helper_clone_no_head(self.linked_list)

    def test_clone_only_head(self):
        head = Node(145)
        self.helper.helper_clone_only_head(self.linked_list, head)

    def test_clone_multiple(self):
        head = Node(99999)
        head.next = Node(4562)
        head.next.next = Node(12353)

        self.helper.helper_clone_multiple(self.linked_list, head)


class DoublyLinkedListTests(unittest.TestCase):

    def setUp(self):
        self.linked_list = DoublyLinkedList()
        self.helper = SharedListTestHelpers()

    def tearDown(self):
        pass

    def test_add_first_no_head(self):
        self.helper.helper_add_first_no_head(self.linked_list, DoublyNode(17))

    def test_add_first_has_head(self):
        old_head = DoublyNode(13)
        new_head = DoublyNode(6)

        self.helper.helper_add_first_has_head(self.linked_list, old_head, new_head)

        self.assertIsNone(self.linked_list.head.prev)
        self.assertEqual(
            self.linked_list.head.next.prev, #Second node's prev
            new_head)

    def test_add_last_no_head(self):
        self.helper.helper_add_last_no_head(self.linked_list, DoublyNode(62))

    def test_add_last_has_head(self):
        second_to_last = DoublyNode(55)
        last_node = DoublyNode(7)

        self.helper.helper_add_last_has_head(self.linked_list, second_to_last, last_node)

        self.assertEqual(last_node.prev, second_to_last)

    def test_add_last_in_list(self):
        head = DoublyNode(123)
        to_be_last_node = DoublyNode(555)

        head.next = to_be_last_node
        to_be_last_node.prev = head

        to_be_last_node.next = DoublyNode(7656)
        to_be_last_node.next.prev = to_be_last_node

        self.linked_list.head = head
        self.helper.helper_add_last_in_list(self.linked_list, to_be_last_node)

        prev_node = None
        current_node = self.linked_list.head

        while current_node.next is not None:
            prev_node = current_node
            current_node = current_node.next
            print(f"{prev_node.data}    {current_node.data}")

        self.assertEqual(prev_node.data, current_node.prev.data)

    def test_print_list_empty(self):
        self.helper.helper_print_list_empty(self.linked_list)

    def test_insert_after_no_head(self):
        self.helper.helper_insert_after_no_head(self.linked_list, DoublyNode(7))

    def test_insert_after_only_head(self):
        prev_node = DoublyNode(1)
        new_node = DoublyNode(11)

        self.helper.helper_insert_after_only_head(self.linked_list, prev_node, new_node)

        self.assertIsNone(self.linked_list.head.prev)
        self.assertEqual(self.linked_list.head, new_node.prev)

    def test_insert_after_after_head(self):
        prev_node = DoublyNode(2)
        new_node = DoublyNode(5)

        self.linked_list.head = DoublyNode(7)
        self.linked_list.head.next = prev_node
        prev_node.prev = self.linked_list.head

        self.helper.helper_insert_after_after_head(self.linked_list, prev_node, new_node)

        self.assertEqual(prev_node.prev, self.linked_list.head)
        self.assertEqual(new_node.prev, prev_node)

    def test_insert_before_no_head(self):
        after_node = DoublyNode(2)
        new_node = DoublyNode(1000)

        self.helper.helper_insert_before_no_head(self.linked_list, after_node, new_node)

    def test_insert_before_only_head(self):
        after_node = DoublyNode(99999)
        new_node = DoublyNode(1246)

        self.helper.helper_insert_before_only_head(self.linked_list, after_node, new_node)

        self.assertIsNone(self.linked_list.head.prev)
        self.assertEqual(after_node.prev, new_node)

    def test_insert_before_after_head(self):
        after_node = DoublyNode(765)
        new_node = DoublyNode(123)

        self.linked_list.head = DoublyNode(3)
        self.linked_list.head.next = after_node
        after_node.prev = self.linked_list.head

        self.helper.helper_insert_before_after_head(self.linked_list, after_node, new_node)

        self.assertEqual(new_node.prev, self.linked_list.head)
        self.assertEqual(after_node.prev, new_node)

    def test_delete_node_no_head(self):
        self.helper.helper_delete_node_no_head(self.linked_list, 900)

    def test_delete_node_only_head(self):
        node_to_delete = DoublyNode(6)
        self.helper.helper_delete_node_only_head(self.linked_list, node_to_delete)

    def test_delete_node_after_head(self):
        head = Node(6)
        after_node = Node(100)
        node_to_delete = Node(8528)

        head.next = node_to_delete
        node_to_delete.prev = head

        node_to_delete.next = after_node
        after_node.prev = node_to_delete

        self.helper.helper_delete_node_after_head(self.linked_list, head, node_to_delete)

        self.assertEqual(after_node.prev, head)

    def test_clone_no_head(self):
        self.helper.helper_clone_no_head(self.linked_list)

    def test_clone_only_head(self):
        head = DoublyNode(145)
        self.helper.helper_clone_only_head(self.linked_list, head)

    def test_clone_multiple(self):
        head = DoublyNode(99999)

        head.next = DoublyNode(4562)
        head.next.prev = head

        head.next.next = DoublyNode(12353)
        head.next.next.prev = head.next

        clone = self.helper.helper_clone_multiple(self.linked_list, head)

        current_clone = clone.head.next
        current_list = head.next

        while current_clone is not None:
            self.assertNotEqual(current_list.prev, current_clone.prev)
            self.assertEqual(current_list.prev.data, current_clone.prev.data)

            current_clone = current_clone.next
            current_list = current_list.next


class SharedListTestHelpers(unittest.TestCase):

    def helper_add_first_no_head(self, list_obj, new_head):
        list_obj.head = None

        list_obj.add_first(new_head)

        self.assertEqual(list_obj.head, new_head)

    def helper_add_first_has_head(self, list_obj, old_head, new_head):
        list_obj.head = old_head
        list_obj.add_first(new_head)

        self.assertEqual(list_obj.head, new_head)
        self.assertEqual(list_obj.head.next, old_head)

    def helper_add_last_no_head(self, list_obj, last_node):
        list_obj.head = None

        list_obj.add_last(last_node)

        self.assertEqual(list_obj.head, last_node)

    def helper_add_last_has_head(self, list_obj, second_to_last, last_node):
        list_obj.head = second_to_last

        list_obj.add_last(last_node)

        self.assertEqual(list_obj.head, second_to_last)
        self.assertEqual(list_obj.head.next, last_node)

    def helper_add_last_in_list(self, list_obj, last_node):
        list_obj.add_last(last_node)

        current_node = list_obj.head

        while current_node.next is not None:
            current_node = current_node.next

        self.assertEqual(current_node, last_node)
        self.assertIsNone(last_node.next)

    def helper_print_list_empty(self, list_obj):
        list_obj.head = None

        printed_values = StringIO()
        sys.stdout = printed_values

        list_obj.print_list()
        sys.stdout = sys.__stdout__ #Reset printing

        self.assertEqual(printed_values.getvalue(), '')

    def helper_insert_after_no_head(self, list_obj, new_node):
        list_obj.head = None

        self.assertIsNone(list_obj.insert_after(15, new_node))

    def helper_insert_after_only_head(self, list_obj, prev_node, new_node):
        list_obj.head = prev_node

        self.assertEqual(list_obj.insert_after(prev_node.data, new_node), prev_node)
        self.assertEqual(list_obj.head, prev_node)
        self.assertEqual(list_obj.head.next, new_node)

    def helper_insert_after_after_head(self, list_obj, prev_node, new_node):
        head = list_obj.head
        self.assertTrue(list_obj.insert_after(prev_node.data, new_node))

        self.assertEqual(list_obj.head, head)
        self.assertEqual(prev_node.next, new_node)

    def helper_insert_before_no_head(self, list_obj, after_node, new_node):
        list_obj.head = None

        self.assertFalse(list_obj.insert_before(after_node.data, new_node))

        self.assertIsNone(list_obj.head)

    def helper_insert_before_only_head(self, list_obj, after_node, new_node):
        list_obj.head = after_node

        self.assertTrue(list_obj.insert_before(after_node.data, new_node))

        self.assertEqual(list_obj.head, new_node)
        self.assertEqual(list_obj.head.next, after_node)

    def helper_insert_before_after_head(self, list_obj, after_node, new_node):
        head = list_obj.head

        self.assertTrue(list_obj.insert_before(after_node.data, new_node))

        self.assertEqual(list_obj.head, head)
        self.assertEqual(new_node.next, after_node)

    def helper_delete_node_no_head(self, list_obj, data_to_delete):
        list_obj.head = None

        self.assertFalse(list_obj.delete_node(data_to_delete))

        self.assertIsNone(list_obj.head)

    def helper_delete_node_only_head(self, list_obj, node_to_delete):
        list_obj.head = node_to_delete

        self.assertTrue(list_obj.delete_node(node_to_delete.data))
        self.assertIsNone(list_obj.head)

    def helper_delete_node_after_head(self, list_obj, head_node, node_to_delete):
        list_obj.head = head_node

        self.assertTrue(list_obj.delete_node(node_to_delete.data))
        self.assertEqual(list_obj.head, head_node)
        self.assertEqual(list_obj.head.next, node_to_delete.next)

    def helper_clone_no_head(self, list_obj):
        list_obj.head = None

        clone = list_obj.clone()

        self.assertNotEqual(list_obj, clone)
        self.assertIsInstance(clone, type(list_obj))

    def helper_clone_only_head(self, list_obj, head):
        list_obj.head = head

        clone = list_obj.clone()

        self.assertIsNotNone(clone.head)
        self.assertEqual(list_obj.head.data, clone.head.data)

        self.assertNotEqual(list_obj, clone)
        self.assertNotEqual(list_obj.head, clone.head)

        self.assertIsInstance(clone, type(list_obj))

    def helper_clone_multiple(self, list_obj, head):
        list_obj.head = head

        clone = list_obj.clone()

        self.assertIsNotNone(clone.head)
        self.assertEqual(list_obj.head.data, clone.head.data)

        self.assertNotEqual(list_obj, clone)

        current_clone = clone.head
        current_list = list_obj.head

        while current_list is not None:
            self.assertNotEqual(current_list, current_clone)
            self.assertEqual(current_list.data, current_clone.data)

            current_clone = current_clone.next
            current_list = current_list.next

        return clone

#TODO: Unit Tests for delete node methods
if __name__ == "__main__":
    unittest.main()