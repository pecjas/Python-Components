import unittest
from binary_search_tree import BinarySearchTree, Node

class BinarySearchTreeTests(unittest.TestCase):
    insert_assertion_params = {
        0: (5, "self.bst.root.data"),
        1: (1, "self.bst.root.left.data"),
        2: (20, "self.bst.root.right.data"),
        3: (10, "self.bst.root.right.left.data")
    }

    sample_tree_values = { #key is level <tree level> - <node position from left most in level>
        "root": 15,

        "level 1-1": 12,
        "level 1-2": 30,

        "level 2-1":  4,
        "level 2-2": 14,
        "level 2-3": 22
    }

    sample_tree_excluded_values = [
        -3,
        0,
        17,
        10000,
        16534324,
        999999999
    ]

    sample_node_values_ascending = [
        6, 10, 15
    ]


    def setUp(self):
        self.bst = BinarySearchTree()

    def tearDown(self):
        pass

    def test_bst_is_empty(self):
        self.bst.root = None
        self.assertTrue(self.bst.is_empty())

        self.bst.root = Node(1)
        self.assertFalse(self.bst.is_empty())


    def test_bst_insert(self):
        self.bst.root = None

        for i in range(len(self.insert_assertion_params)):
            self._insert_assertion_value(i)
            self._evaluate_insert_assertion_attribute(i)

    def _insert_assertion_value(self, key: int):
        value_to_insert = self.insert_assertion_params.get(key)[0]
        return self.bst.insert(value_to_insert)

    def _evaluate_insert_assertion_attribute(self, key: int):
        current_value = eval(str(self.insert_assertion_params.get(key)[1]))
        return self.assertEqual(current_value, self.insert_assertion_params.get(key)[0])


    def test_bst_find(self):
        self._populate_sample_tree()

        for tree_data in BinarySearchTreeTests.sample_tree_values.values():
            self.assertTrue(self.bst.find(tree_data))

        for not_tree_data in BinarySearchTreeTests.sample_tree_excluded_values:
            self.assertFalse(self.bst.find(not_tree_data))

    def _populate_sample_tree(self):
        """
            Tree structure:
                        15

                12              30

            4       14      22
        """
        self.bst.root = Node(BinarySearchTreeTests.sample_tree_values.get("root"))

        root_left = Node(BinarySearchTreeTests.sample_tree_values.get("level 1-1"))
        root_right = Node(BinarySearchTreeTests.sample_tree_values.get("level 1-2"))
        self.bst.root.left = root_left
        self.bst.root.right = root_right

        root_left.left = Node(BinarySearchTreeTests.sample_tree_values.get("level 2-1"))
        root_left.right = Node(BinarySearchTreeTests.sample_tree_values.get("level 2-2"))

        root_right.left = Node(BinarySearchTreeTests.sample_tree_values.get("level 2-3"))


    def test_bst_remove_value_not_found(self):
        self.bst.root = None

        self.assertFalse(self.bst.remove(1))

    def test_bst_remove_root_no_children(self):
        self.bst.root = Node(7)

        self.assertTrue(self.bst.remove(7))
        self.assertIsNone(self.bst.root)


    def test_bst_remove_root_left_child_only(self):
        self._test_bst_remove_one_child_helper("left")

    def test_bst_remove_root_right_child_only(self):
        self._test_bst_remove_one_child_helper("right")

    def _test_bst_remove_one_child_helper(self, child: str):
        self.bst.root = Node(36)
        setattr(self.bst.root, child, Node(16))

        self.assertTrue(self.bst.remove(36))
        self.assertEqual(self.bst.root.data, 16)


    def test_bst_remove_root_full(self):
        self._populate_sample_tree()
        self.assertTrue(self.bst.remove(BinarySearchTreeTests.sample_tree_values.get("root")))

        left_child = self.bst.root.left
        right_child = self.bst.root.right

        self.assertEqual(self.bst.root.data, BinarySearchTreeTests.sample_tree_values.get("level 2-3"))

        self.assertEqual(left_child.data, BinarySearchTreeTests.sample_tree_values.get("level 1-1"))
        self.assertEqual(right_child.data, BinarySearchTreeTests.sample_tree_values.get("level 1-2"))

        self.assertEqual(left_child.left.data, BinarySearchTreeTests.sample_tree_values.get("level 2-1"))
        self.assertEqual(left_child.right.data, BinarySearchTreeTests.sample_tree_values.get("level 2-2"))

        self.assertIsNone(right_child.left)
        self.assertIsNone(right_child.right)


    def test_bst_remove_not_root(self):
        self._populate_sample_tree()
        node_to_remove = "level 2-1"

        self.assertTrue(self.bst.remove(BinarySearchTreeTests.sample_tree_values.get(node_to_remove)))

        self.assertEqual(self.bst.root.data, BinarySearchTreeTests.sample_tree_values.get("root"))

        left_child = self.bst.root.left
        right_child = self.bst.root.right

        self.assertEqual(left_child.data, BinarySearchTreeTests.sample_tree_values.get("level 1-1"))
        self.assertEqual(right_child.data, BinarySearchTreeTests.sample_tree_values.get("level 1-2"))

        self.assertIsNone(left_child.left)
        self.assertEqual(left_child.right.data, BinarySearchTreeTests.sample_tree_values.get("level 2-2"))

        self.assertEqual(right_child.left.data, BinarySearchTreeTests.sample_tree_values.get("level 2-3"))
        self.assertIsNone(right_child.right)


    def test_bst_traverse_pre_order(self):
        self._populate_sample_tree()
        self.assertEqual(self.bst.traverse_pre_order(),
                         BinarySearchTreeTests._get_sample_tree_pre_order())

    @classmethod
    def _get_sample_tree_pre_order(cls):
        return [
            cls.sample_tree_values.get("root"),
            cls.sample_tree_values.get("level 1-1"),
            cls.sample_tree_values.get("level 2-1"),
            cls.sample_tree_values.get("level 2-2"),
            cls.sample_tree_values.get("level 1-2"),
            cls.sample_tree_values.get("level 2-3")
        ]


    def test_bst_traverse_in_order(self):
        self._populate_sample_tree()
        self.assertEqual(self.bst.traverse_in_order(), self._get_sample_tree_in_order())

    @classmethod
    def _get_sample_tree_in_order(cls):
        return [
            cls.sample_tree_values.get("level 2-1"),
            cls.sample_tree_values.get("level 1-1"),
            cls.sample_tree_values.get("level 2-2"),
            cls.sample_tree_values.get("root"),
            cls.sample_tree_values.get("level 2-3"),
            cls.sample_tree_values.get("level 1-2")
        ]


    def test_bst_traverse_post_order(self):
        self._populate_sample_tree()
        self.assertEqual(self.bst.traverse_post_order(), self._get_sample_tree_post_order())

    @classmethod
    def _get_sample_tree_post_order(cls):
        return [
            cls.sample_tree_values.get("level 2-1"),
            cls.sample_tree_values.get("level 2-2"),
            cls.sample_tree_values.get("level 1-1"),
            cls.sample_tree_values.get("level 2-3"),
            cls.sample_tree_values.get("level 1-2"),
            cls.sample_tree_values.get("root")
        ]


    def test_node_is_without_child(self):
        self._verify_function_meets_boolean_with_each_type_of_parenthood("node.is_without_child()", False)

    def test_node_is_with_child(self):
        self._verify_function_meets_boolean_with_each_type_of_parenthood("node.is_with_child()", True)

    def test_node_is_with_exactly_one_child(self):
        self._verify_function_meets_boolean_with_each_type_of_parenthood("node.is_with_exactly_one_child()", True, True)

    def _verify_function_meets_boolean_with_each_type_of_parenthood(self, function, bool_check, not_both=False):
        node = BinarySearchTreeTests._get_node_without_children(16)

        self.assertEqual(eval(function), not bool(bool_check)) #Initial check - opposite bool since no children

        node.left = Node(6)

        self.assertEqual(eval(function), bool(bool_check))

        node.left = None
        node.right = Node(14)

        self.assertEqual(eval(function), bool(bool_check))

        node.left = Node(6)

        if not_both:
            bool_check = not bool_check

        self.assertEqual(eval(function), bool(bool_check))

    @staticmethod
    def _get_node_without_children(val):
        node = Node(val)
        node.left = None
        node.right = None

        return node


    def test_node_insert_self(self):
        node = Node(15)
        self.assertFalse(node.insert(15))

    def test_node_insert_left(self):
        node = Node(10)
        node.left = Node(6)
        insert_value = 2

        self.assertTrue(node.insert(insert_value))
        self.assertEqual(node.left.left.data, insert_value)

    def test_node_insert_right(self):
        node = Node(43)
        insert_value = 600

        self.assertTrue(node.insert(insert_value))
        self.assertEqual(node.right.data, insert_value)


    def test_node_find_not_found(self):
        node = self._get_full_node()

        self.assertFalse(node.find(-100))
        self.assertFalse(node.find(0))
        self.assertFalse(node.find(99999999))

    def test_node_find_this_node(self):
        node = self._get_full_node()
        self.assertTrue(node.find(node.data))

    def test_node_find_node_left(self):
        node = self._get_full_node()
        self.assertTrue(node.find(node.left.data))

    def test_node_find_node_right(self):
        node = self._get_full_node()
        self.assertTrue(node.find(node.right.data))

    @classmethod
    def _get_full_node(cls):
        node = Node(cls.sample_node_values_ascending[1])
        node.left = Node(cls.sample_node_values_ascending[0])
        node.right = Node(cls.sample_node_values_ascending[2])

        return node


    def test_node_traverse_pre_order(self):
        node = self._get_full_node()
        self.assertEqual(node.traverse_pre_order([]),
                         BinarySearchTreeTests._get_sample_node_tree_pre_order())

    @classmethod
    def _get_sample_node_tree_pre_order(cls):
        return [
            cls.sample_node_values_ascending[1],
            cls.sample_node_values_ascending[0],
            cls.sample_node_values_ascending[2]
        ]


    def test_node_traverse_in_order(self):
        node = self._get_full_node()
        self.assertEqual(node.traverse_in_order([]),
                         BinarySearchTreeTests._get_sample_node_tree_in_order())

    @classmethod
    def _get_sample_node_tree_in_order(cls):
        return [
            cls.sample_node_values_ascending[0],
            cls.sample_node_values_ascending[1],
            cls.sample_node_values_ascending[2]
        ]


    def test_node_traverse_post_order(self):
        node = self._get_full_node()
        self.assertEqual(node.traverse_post_order([]),
                         BinarySearchTreeTests._get_sample_node_tree_post_order())

    @classmethod
    def _get_sample_node_tree_post_order(cls):
        return [
            cls.sample_node_values_ascending[0],
            cls.sample_node_values_ascending[2],
            cls.sample_node_values_ascending[1]
        ]

if __name__ == "__main__":
    unittest.main()
