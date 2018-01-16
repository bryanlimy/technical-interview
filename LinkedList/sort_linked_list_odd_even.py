# Given a linked list, put all the odd elements in lexicographical order list
# in front of the even elements in lexicographical order in place.
import random
from util import *

def sort_linked_list(head):
    odd = None
    odd_tail = None
    even = None

    while head:
        new = Node(head.value)
        if head.value % 2 == 0:
            if not even or even.value >= new.value:
                new.next = even
                even = new
            else:
                prev = even
                next = even.next
                while next and next.value < new.value:
                    prev = prev.next
                    next = next.next
                new.next = next
                prev.next = new
        else:
            if not odd or odd.value >= new.value:
                new.next = odd
                odd = new
            else:
                prev = odd
                next = odd.next
                while next and next.value < new.value:
                    prev = prev.next
                    next = next.next
                new.next = next
                prev.next = new
            if not new.next:
                odd_tail = new
        head = head.next

    if odd_tail:
        odd_tail.next = even
    return odd

if __name__ == "__main__":
    sample = [5, 9, 7, 4, 1, 3, 0, 8, 2, 6]
    head = create_linked_list(sample)
    head.print()
    sorted = sort_linked_list(head)
    sorted.print()
