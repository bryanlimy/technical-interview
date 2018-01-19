from util import *


def reverse(head):
    current = head
    previous = None
    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous


if __name__ == "__main__":
    sample = [1,2,3,4]
    head = create_linked_list(sample)
    head.print()
    reversed = reverse(head)
    reversed.print()
