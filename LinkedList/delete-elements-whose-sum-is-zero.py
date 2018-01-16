# Given a linked list, remove consecutive nodes that sums up to zero
# https://www.careercup.com/question?id=5717797377146880

from util import *

def remove_zero_sum(head):
    start = head
    while start:
        end = start.next
        total = start.value
        while end:
            total += end.value
            if total == 0:
                if head == start:
                    head = end.next
                elif head.next == start:
                    head.next = end.next
                start = end
                break
            end = end.next
        start = start.next
    return head

if __name__ == "__main__":

    s1 = [6, -6, 8, 4, -12, 9, 8, -8]
    s2 = [4, 6 - 10, 8, 9, 10, -19, 10, -18, 20, 25]
    s3 = [2, 3, -5, 10, 10, -5, -5, 20, 5, -5]
    samples = [s3]
    for sample in samples:
        head = create_linked_list(sample)
        print(linked_list_to_list(head))
        head = remove_zero_sum(head)
        print(linked_list_to_list(head))
        print("\n")
