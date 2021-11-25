import random


class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class LinkedList(object):
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def insert(self, data):
        tmp = Node(data)
        tmp.next_node = None
        if self.head is None:
            self.head = tmp
            self.tail = self.head
            self.size += 1
        else:
            self.tail.next_node = tmp
            self.tail = self.tail.next_node
            self.size += 1

    # Find the first element that matches
    def delete(self, data):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == data:
                previous_node.next_node = current_node.next_node
                if current_node is self.tail:
                    self.tail = previous_node
                return current_node
            else:
                previous_node = current_node
                current_node = current_node.next_node
        return None


# Start Main Program
if __name__ == "__main__":
    linkedList = LinkedList()
    # insert some random values
    for n in range(5):
        linkedList.insert(random.randint(1, 100))

    linkedList.insert(5)

    linkedList.delete(50)
