class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)

        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        return False

    def remove(self, data):
        if self.is_empty():
            return False

        elif self.root.data == data:
            return self._delete_root_node()

        else:
            return self._find_and_delete_node(data)

    def is_empty(self):
        return self.root is None

    def _delete_root_node(self):
        if self.root.is_without_child():
            self.root = None
            return True

        elif self.root.is_with_exactly_one_child():
            return self._delete_root_node_with_one_child()

        else:
            return self._delete_root_node_with_two_children()

    def _delete_root_node_with_one_child(self):
        if self.root.is_with_left_child():
            self.root = self.root.left
            return True

        else:
            self.root = self.root.right
            return True

    def _delete_root_node_with_two_children(self):
        node_to_move = self.root.right
        parent_of_node_to_move = None

        while node_to_move.left:
            parent_of_node_to_move = node_to_move
            node_to_move = node_to_move.left

        self.root.data = node_to_move.data

        if node_to_move.data < parent_of_node_to_move.data:
            parent_of_node_to_move.left = None
        else:
            parent_of_node_to_move.right = None
        return True

    def _find_and_delete_node(self, data):
        node, parent = self._find_node_to_delete_and_parent(data)

        if self._is_node_to_delete_not_found(node, data):
            return False

        elif node.is_without_child():
            return self._delete_node_found_without_children(data, parent)

        elif node.is_with_exactly_one_child():
            return self._delete_node_found_with_one_child(node, data, parent)

        else:
            return self._delete_node_found_with_two_children(node)

    def _find_node_to_delete_and_parent(self, data):
        parent = None
        node = self.root

        while node and node.data != data:
            parent = node
            if data < node.data:
                node = node.left

            elif data > node.data:
                node = node.right

        return node, parent

    def _is_node_to_delete_not_found(self, node, data):
        return node is None or node.data != data

    def _delete_node_found_without_children(self, data, parent):
        if data < parent.data:
            parent.left = None
        else:
            parent.right = None
        return True

    def _delete_node_found_with_one_child(self, node, data, parent):
        if node.is_with_left_child():
            if data < parent.data:
                parent.left = node.left
            else:
                parent.right = node.left
            return True

        elif node.is_with_right_child():
            if data < parent.data:
                parent.left = node.right
            else:
                parent.right = node.right

            return True

    def _delete_node_found_with_two_children(self, node):
        parent_of_node_to_move = node
        node_to_move = node.right

        while node_to_move.left:
            parent_of_node_to_move = node_to_move
            node_to_move = node_to_move.left

        node.data = node_to_move.data
        if node_to_move.right:
            if node_to_move.data < parent_of_node_to_move.data:
                parent_of_node_to_move.left = node_to_move.right
            else:
                parent_of_node_to_move.right = node_to_move.right

        else:
            if node_to_move.data < parent_of_node_to_move.data:
                parent_of_node_to_move.left = None
            else:
                parent_of_node_to_move.right = None
        return True

    def traverse_pre_order(self):
        if self.root:
            return self.root.traverse_pre_order([])

        return []

    def traverse_in_order(self):
        if self.root:
            return self.root.traverse_in_order([])

        return []

    def traverse_post_order(self):
        if self.root:
            return self.root.traverse_post_order([])

        return []

class Node():
    def __init__(self, data):
        self.data = data

        self.left = None
        self.right = None

    def is_without_child(self):
        return self.is_with_child() is False

    def is_with_child(self):
        return self.is_with_left_child() or self.is_with_right_child()

    def is_with_exactly_one_child(self):
        return self.is_with_left_child() is not self.is_with_right_child()

    def is_with_left_child(self):
        return self.left is not None

    def is_with_right_child(self):
        return self.right is not None

    def insert(self, data):
        if self.data == data:
            return False

        elif data < self.data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True

        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def find(self, data):
        if self.data == data:
            return True

        elif data < self.data and self.left:
            return self.left.find(data)

        elif data > self.data and self.right:
            return self.right.find(data)

        return False

    def traverse_pre_order(self, all_elements_so_far):
        all_elements_so_far.append(self.data)

        if self.left:
            self.left.traverse_pre_order(all_elements_so_far)

        if self.right:
            self.right.traverse_pre_order(all_elements_so_far)

        return all_elements_so_far

    def traverse_in_order(self, all_elements_so_far):
        if self.left:
            self.left.traverse_in_order(all_elements_so_far)

        all_elements_so_far.append(self.data)

        if self.right:
            self.right.traverse_in_order(all_elements_so_far)

        return all_elements_so_far

    def traverse_post_order(self, all_elements_so_far):
        if self.left:
            self.left.traverse_post_order(all_elements_so_far)

        if self.right:
            self.right.traverse_post_order(all_elements_so_far)

        all_elements_so_far.append(self.data)

        return all_elements_so_far
