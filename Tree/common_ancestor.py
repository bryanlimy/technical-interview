from util import *

def common_ancestor(root, node1, node2):
    if not root:
        return None

    if root.value == node1 or root.value == node2:
        return root
    left = common_ancestor(root.left, node1, node2)
    right = common_ancestor(root.right, node1, node2)

    if left and right:
        return root

    return left if left else right

if __name__ == "__main__":
    lst = [4, 8, 2, 5, 1, 6, 3, 7]
    root = create_bst(lst)

    print(root.preorder())
    print(root.inorder())

    ancestor = common_ancestor(root, 8, 1)
    print(ancestor.value)