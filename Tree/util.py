class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = Node(value)
            else:
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = Node(value)
        else:
            self.value = value

    def preorder(self):
        result = []
        if not self:
            return result
        result.append(self.value)
        if self.left:
            result += self.left.preorder()
        if self.right:
            result += self.right.preorder()
        return result

    def inorder(self):
        result = []
        if not self:
            return result
        if self.left:
            result += self.left.inorder()
        result.append(self.value)
        if self.right:
            result += self.right.inorder()
        return result

    def postorder(self):
        result = []
        if not self:
            return result
        if self.left:
            result += self.left.postorder()
        if self.right:
            result += self.right.postorder()
        result.append(self.value)
        return result


def create_bst(lst):
    root = Node(lst[0])
    for i in lst[1:]:
        root.insert(i)
    return root
