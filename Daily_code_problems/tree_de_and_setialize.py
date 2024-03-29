# Problem Number 3

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#    def __init__(self, val, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right
# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node: Node):
    if node.left is not None:
        serialize(node.left)
    if node.right is not None:
        serialize(node.right)
    return node.val


def deserialize(node: Node):
    pass


node = Node('root', Node('left'
                         , Node('left.left')),
            Node('right'))

print(serialize(node))

assert deserialize(serialize(node)).left.left.val == 'left.left'
