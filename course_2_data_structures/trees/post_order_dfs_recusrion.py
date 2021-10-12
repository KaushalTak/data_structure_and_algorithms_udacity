# this code makes the tree that we'll traverse

class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


def post_order(tree):
    node = tree.get_root()
    visit_order = []
    a = post_order_rec(node, visit_order)
    return visit_order


def post_order_rec(node, visit_order):
    if node:
        post_order_rec(node.get_left_child(), visit_order)
        post_order_rec(node.get_right_child(), visit_order)
        visit_order.append(node.get_value())


if __name__ == '__main__':
    # create a tree and add some nodes
    tree = Tree("apple")
    tree.get_root().set_left_child(Node("banana"))
    tree.get_root().set_right_child(Node("cherry"))
    tree.get_root().get_left_child().set_left_child(Node("dates"))
    tree.get_root().get_left_child().set_right_child(Node('After banana'))
    print(post_order(tree))
