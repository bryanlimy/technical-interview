from util import *

def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

if __name__ == "__main__":
    sample = [1,2,3,4,5,6,7,8,9]
    head = create_linked_list(sample)
    middle = find_middle(head)
    print(middle.value)
