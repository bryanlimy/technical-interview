from util import *
from find_middle import find_middle

def sort_linked_list(head):
    sorted = None
    while head:
        node = Node(head.value)
        if not sorted or sorted.value >= node.value:
            node.next = sorted
            sorted = node
        else:
            current = sorted
            while current.next and current.next.value < node.value:
                current = current.next
            node.next = current.next
            current.next = node
        head = head.next
    return sorted


def merge_linked_list(head1, head2):
    if not head1:
        return head2
    
    if not head2:
        return head1

    if head1.value <= head2.value:
        new_head = head1
        new_head.next = merge_linked_list(head1.next, head2)
    else:
        new_head = head2
        new_head.next = merge_linked_list(head1, head2.next)

    return new_head


def merge_sort_linked_list(head):
    if not head or not head.next:
        return head

    mid = find_middle(head)
    next_of_mid = mid.next

    mid.next = None

    head1 = merge_sort_linked_list(head)
    head2 = merge_sort_linked_list(next_of_mid)

    return merge_linked_list(head1, head2)


if __name__ == "__main__":
    sample = [5, 9, 7, 4, 1, 3, 0, 8, 2, 6]
    head = create_linked_list(sample)
    head.print()
    sorted = sort_linked_list(head)
    sorted.print()
    merge_sorted = merge_sort_linked_list(head)
    merge_sorted.print()
