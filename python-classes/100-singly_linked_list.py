#!/usr/bin/python3
"""Singly linked list with Node and sorted insertion."""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list (increasing order)."""

    def __init__(self):
        self.__head = None  # private, no getter/setter

    def __str__(self):
        lines = []
        current = self.__head
        while current is not None:
            lines.append(str(current.data))
            current = current.next_node
        return "\n".join(lines)

    def sorted_insert(self, value):
        """Insert a new Node in increasing order."""
        new_node = Node(value)

        # Insert at head if list is empty or value is smallest
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Walk to insertion point
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
