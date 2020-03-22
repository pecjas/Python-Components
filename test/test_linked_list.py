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

#TODO: Unit Tests for delete node methods
