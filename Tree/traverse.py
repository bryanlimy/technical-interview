from util import *

def DFS_recursive(head, visited=[]):
    if not head:
        return None
    visited.append(head.value)
    for node in [head.left, head.right]:
        if node:
            DFS_recursive(node, visited)
    return visited

def DFS_iterative(head):
    if not head:
        return None
    current, visited = [head], []
    while current:
        node = current.pop()
        visited.append(node.value)
        if node.right:
            current.append(node.right)
        if node.left:
            current.append(node.left)
    return visited


def inorder_without_recursion(head):
    current = head
    stack = []
    done = False
    while not done:
        # keep traversing to the left
        # then to the right
        if current:
            stack.append(current)
            current = current.left
        else:
            if stack:
                current = stack.pop()
                print(current.value)
                current = current.right
            else:
                done = True


if __name__ == "__main__":
    lst = [4, 8, 2, 5, 1, 6, 3, 7]
    root = create_bst(lst)
    print(root.preorder())
    print(root.inorder())
    print(root.postorder())

    print(DFS_recursive(root, []))
    print(DFS_iterative(root))

    inorder_without_recursion(root)
