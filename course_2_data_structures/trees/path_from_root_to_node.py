class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def path_from_root_to_node(root, data):
    """
    :param: root - root of binary tree
    :param: data - value (representing a node)
    TODO: complete this method and return a list containing values of each node in the path
    from root to the data node
    """
    return list(reversed(path_from_node_to_root(root, data)))


def path_from_node_to_root(root, data):
    if root is None:
        return None
    elif root.data == data:
        return [data]
    left_ans = path_from_node_to_root(root.left, data)
    if left_ans is not None:
        left_ans.append(root.data)
        return left_ans
    right_ans = path_from_node_to_root(root.right, data)
    if right_ans is not None:
        right_ans.append(root.data)
        return right_ans
    return None
