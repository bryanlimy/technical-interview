# Given Post-order and In-order traversals, construct the tree.
# See https://www.geeksforgeeks.org/construct-a-binary-tree-from-postorder-and-inorder/ fpr detail

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def preorder(self):
        if not self:
            return []
        result = [self.value]
        if self.left:
            result += self.left.preorder()
        if self.right:
            result += self.right.preorder()
        return result


def construct(inorder, postorder):
    if not inorder or not postorder or len(inorder) != len(postorder):
        return None
    # get root value from post-order
    root = Node(postorder[-1])
    # get index of root in in-order
    index = inorder.index(root.value)
    # get the in-order list of root.left and root.right
    left_in = inorder[:index]
    right_in = inorder[index + 1:]
    # get the post-order list of root.left and root.right
    left_post = postorder[:len(postorder) - len(right_in) - 1]
    right_post = postorder[len(left_in): -1]
    # recursively construct root.left and root.right
    root.left = construct(left_in, left_post)
    root.right = construct(right_in, right_post)
    return root


if __name__ == "__main__":
    inorder = [4, 8, 2, 5, 1, 6, 3, 7]
    postorder = [8, 4, 5, 2, 6, 7, 3, 1]
    node = construct(inorder, postorder)
    print(node.preorder())
