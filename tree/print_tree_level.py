from util import *


def print_level_reverse(root):
    """ print tree level by level, in reverse order every one level"""
    current_level = [root]
    level = 1
    while current_level:
        next_level = []
        for node in current_level[::level]:
            print(node.value, end=" ")

        for node in current_level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level = 1 if level == -1 else -1
        print("")
        current_level = next_level


def print_level(root):
    """ print tree level by level """
    current_level = [root]
    while current_level:
        next_level = []
        for node in current_level:
            print(node.value, end=" ")
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        print("")
        current_level = next_level


if __name__ == "__main__":
    lst = [4, 8, 2, 5, 1, 6, 3, 7]
    root = create_bst(lst)

    print_level(root)
    print("")
    print_level_reverse(root)
