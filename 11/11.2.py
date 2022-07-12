"""
Aufgabe:

Implement a function invert(root) that inverts a tree. Hint: using recursion, your code will be less
than 10 lines.

@Chaitanya
Kommentar: invert Methode implementiert
"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()


def invert(root):
    if root.left:
        invert(root.left)
    if root.right:
        invert(root.right)
    temp = root.left
    root.left = root.right
    root.right = temp


if __name__ == '__main__':
    root = Node('F')
    for v in 'BADCEGIH':
        root.insert(v)

    invert(root)
    root.inorder()
