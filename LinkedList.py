import random

from typing import Optional

class Node:
    def __init__(self, data: Optional[int]=None):
        self.data = data
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None

class LinkedList:

    def __init__(self) -> None:
        self.size = 0
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, data: int) -> None:
        node = Node(data)
        last_elm = self.tail.prev
        last_elm.next = node
        node.next = self.tail
        node.prev = last_elm
        self.tail.prev = node

    # Find the first element that matches
    # def delete(self, data):
    #     current_node = self.head
    #     previous_node = None
    #     while current_node is not None:
    #         if current_node.data == data:
    #             previous_node.next = current_node.next
    #             if current_node is self.tail:
    #                 self.tail = previous_node
    #             return current_node
    #         else:
    #             previous_node = current_node
    #             current_node = current_node.next
    #     return None

# Start Main Program
if __name__ == "__main__":
    linkedList = LinkedList()
    # insert some random values
    for n in range(5):
        linkedList.insert(random.randint(1, 100))

    linkedList.insert(5)

    # linkedList.delete(50)
