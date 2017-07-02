class tree_node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def add_node(self, node_left, node_right):
        self.left = node_left
        self.right = node_right


def max_height(root):
    if root == None:
        return 0
    else:
        return (1 + max(max_height(root.right), max_height(root.left)))


if __name__ == '__main__':
    tree = tree_node(10)
    tree.right = tree_node(12)
    tree.left = tree_node(1)
    tree.left.left = tree_node(4)
    tree.left.right = tree_node(5)
    tree.left.right.right = tree_node(8)

    print max_height(tree)
