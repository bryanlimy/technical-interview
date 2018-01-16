class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def print(self):
        print(linked_list_to_list(self))


def create_linked_list(lst):
    if not lst:
        return None
    node = Node(lst[0])
    node.next = create_linked_list(lst[1:])
    return node


def linked_list_to_list(node):
    if not node:
        return []
    return [node.value] + linked_list_to_list(node.next)
