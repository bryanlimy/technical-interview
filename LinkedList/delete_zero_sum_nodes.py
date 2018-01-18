# Given a linked list, remove consecutive nodes that sums up to zero
# https://www.careercup.com/question?id=5717797377146880

from util import *

def remove_zero_sum(head):
    start = head
    new = None
    root = None
    while start:
        end = start.next
        total = start.value
        zero = False
        while end:
            total += end.value
            if total == 0:
                zero = True
                start = end
                break
            end = end.next
        if not zero and not new:
            new = Node(start.value)
            root = new
        elif not zero and new:
            new.next = Node(start.value)
        start = start.next

    return root

if __name__ == "__main__":

    s1 = [6, -6, 8, 4, -12, 9, 8, -8]
    s2 = [4, 6 - 10, 8, 9, 10, -19, 10, -18, 20, 25]
    s3 = [2, 3, -5, 10, 10, -5, -5, 20, 5, -5]
    samples = [s1,s2,s3]
    for sample in samples:
        head = create_linked_list(sample)
        print(linked_list_to_list(head))
        result = remove_zero_sum(head)
        print(linked_list_to_list(result))
        print("\n")
