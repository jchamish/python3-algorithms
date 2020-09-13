import itertools

def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def partition_2(array, low, high):
    i = (low - 1)
    povit = array[high]

    for j in range(low, high):
        if array[j] <= povit:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1





def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def isValid(s: str) -> bool:
    if len(s) < 2:
        return False
    keys = {'(': ')', '{': '}', '[': ']'}
    stack = []

    for char in s:
        if char in keys:
            stack.append(char)
        elif len(stack) > 0 and keys[stack[-1]] == char:
            stack.pop()
    return len(stack) == 0


# test id 23280666885493


class Node(object):
    def __init__(self, val=0, left=None, right=None, depth=0):
        self.left = left
        self.right = right
        self.val = val
        self.depth = depth


def bstDistance(num, values, node1, node2):
    # WRITE YOUR CODE HERE

    # set the root to the first element
    root = Node(val=values.pop(0), depth=0)
    # insert each element
    for i in values:
        bstInsert(root, Node(i), 0)

    # find node 1
    node1_obj = bstSearch(root, node1)
    # find node 2
    node2_obj = bstSearch(root, node2)
    print(
        type(node1_obj)
    )
    # print(node2_obj)
    return -1


def bstInsert(root, node, depth):
    if root is None:
        root = node
    else:
        # left have is great then right have of tree
        if root.val < node.val:
            if root.right is None:
                node.depth = depth
                root.right = node
            else:
                bstInsert(root.right, node, depth + 1)
        else:
            if root.left is None:
                node.depth = depth
                root.left = node
            else:
                bstInsert(root.left, node, depth + 1)


def bstSearch(root, key):
    # check if root is none
    if root is None or root.val == key:
        return root

    if root.val < key:
        return bstSearch(root.right, key)

    if root.val > key:
        return bstSearch(root.left, key)


# bstDistance(6, [5,6,3,1,2,4], 2, 4)


#return list(itertools.chain(*[[nums[idx + 1]] * nums[idx] for idx, freq in enumerate(nums[::2])]))

# list(itertools.chain(*[ ]))