class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def linkedlist2list(self):
        lst = []
        if self:
            lst += [self.value]
        if self and self.next:
            lst += self.next.linkedlist2list()
        return lst


def create_linkedlist(lst):
    if not lst:
        return None
    node = Node(lst[0])
    node.next = create_linkedlist(lst[1:])
    return node


def remove_zero(head):
    start = head
    while start:
        end = start.next
        total = start.value
        modified = False
        while end:
            total += end.value
            if total == 0:
                modified = True
                start = end.next
                break
            end = end.next
        if not modified:
            start = start.next
    return head

if __name__ == "__main__":
    sample = [6, -6, 8, 4, -12, 9, 8, -8]
    head = create_linkedlist(sample)
    print(head.linkedlist2list())

    new = remove_zero(head)
    print(new.linkedlist2list())
