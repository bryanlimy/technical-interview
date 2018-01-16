from util import *


def sort_linked_list(head):
    sorted = None
    while head:
        node = Node(head.value)
        if not sorted or sorted.value >= node.value:
            node.next = sorted
            sorted = node
        else:
            prev = sorted
            next = sorted.next
            while next and next.value < node.value:
                prev = prev.next
                next = next.next
            node.next = next
            prev.next = node
        head = head.next
    return sorted


if __name__ == "__main__":
    sample = [5, 9, 7, 4, 1, 3, 0, 8, 2, 6]
    head = create_linked_list(sample)
    head.print()
    sorted = sort_linked_list(head)
    sorted.print()
