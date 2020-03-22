##TODO: Note - this is still in progress

class Node():
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def print_list(self):
        node = self.head

        while node  is not None:
            print(node.data)
            node = node.next

    def add_first(self, new_head):
        if self.is_head_node(new_head):
            return

        new_head.next = self.head
        self.head = new_head

    def is_head_node(self, node):
        return self.head == node

    def add_last(self, last_node):
        """
        Returns second to last node. Used for double linked list inheritence.
        """
        if self.head is None:
            self.add_first(last_node)
            return

        runner = self.head
        while runner.next is not None:
            #TODO: Add check if we find node as we go. If so, remove and add to end
            # We don't want the SAME node in multiple positions, but we can have multiple
            # nodes with the same data.
            runner = runner.next

        runner.next = last_node
        return runner

    def insert_after(self, prev_data, new_node):
        """
        Returns None if prev_data can't be found in list. Otherwise, returns node containing prev_data.
        """
        if self.head is None:
            return None

        runner = self.head
        while runner.data != prev_data and runner is not None:
            runner = runner.next

        if runner is not None:
            new_node.next = runner.next
            runner.next = new_node
            return runner

        return None

    def insert_before(self, data_after, new_node) -> bool:
        """
        Returns False if prev_data can't be found in list. Otherwise, returns True.
        """
        if self.head is None:
            return False

        if self.head.data == data_after:
            new_node.next = self.head
            self.head = new_node
            return True

        prev_node, current_node = self._traverse_to_node_with_prev(data_after)

        if current_node.data == data_after:
            prev_node.next = new_node
            new_node.next = current_node
            return True

        return False

    def delete_node(self, data_to_delete) -> bool:
        """
        Returns False if data_to_delete can't be found in list. Otherwise, deletes node and returns True.
        """
        if self.head is None:
            return False

        if self.head.data == data_to_delete:
            self.head = None
            return True

        prev_node, current_node = self._traverse_to_node_with_prev(data_to_delete)

        if current_node is None:
            return False

        prev_node.next = current_node.next
        return True

    def _traverse_to_node_with_prev(self, data_to_find):
        current_node = self.head
        prev_node = None

        while current_node.data != data_to_find and current_node is not None:
            prev_node = current_node
            current_node = current_node.next

        return prev_node, current_node














class DoublyNode(Node):
    def __init__(self, data, next_=None, prev=None):
        super().__init__(data, next_)

        self.prev = prev

class DoublyLinkedList(LinkedList):
    def add_first(self, new_head):
        old_head = self.head

        super().add_first(new_head)

        if not super().is_head_node(old_head) and old_head is not None:
            old_head.prev = new_head

    def add_last(self, last_node):
        """
        Returns second to last node for consistency with Linked List.
        """
        second_last_node = super().add_last(last_node)

        last_node.prev = second_last_node
        return second_last_node

    def insert_after(self, prev_data, new_node):
        """
        Returns None if prev_data can't be found in list. Otherwise, returns node containing prev_data.
        """
        prev_node = super().insert_after(prev_data, new_node)

        if prev_node is None:
            return None

        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node

        return prev_node

    def insert_before(self, data_after, new_node):
        """
        Returns False if prev_data can't be found in list. Otherwise, returns True.
        """
        if self.head is None:
            return False

        if self.head.data == data_after:
            new_node.next = self.head
            self.head.prev = new_node

            self.head = new_node
            return True

        current_node = self._traverse_to_node(data_after)

        if current_node.data == data_after:
            new_node.prev = current_node.prev
            new_node.next = current_node

            current_node.prev.next = new_node
            current_node.prev = new_node
            return True

        return False

    def _traverse_to_node(self, data_to_find):
        current_node = self.head

        while current_node.data != data_to_find and current_node is not None:
            current_node = current_node.next

        return current_node

    def delete_node(self, data_to_delete) -> bool:
        """
        Returns False if data_to_delete can't be found in list. Otherwise, deletes node and returns True.
        """
        if self.head is None:
            return False

        if self.head.data == data_to_delete:
            self.head = None
            return True

        current_node = self._traverse_to_node(data_to_delete)

        if current_node is None:
            return False

        current_node.prev.next = current_node.next
        return True
