"""
Aufgabe:

Review the tree implementation in Algorithm 3. Extend it by implementing traversal
methods for pre-order and post-order, both as generators and without generators, respectively.

@Chaitanya
Kommentar: Easy
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

    def pre_order(self):
        print(self.data)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.data)

    def inorder_generator(self):
        if self.left:
            yield from self.left.inorder_generator()
        yield self.data
        if self.right:
            yield from self.right.inorder_generator()

    def pre_order_generator(self):
        yield self.data
        if self.left:
            yield from self.left.pre_order_generator()
        if self.right:
            yield from self.right.pre_order_generator()

    def post_order_generator(self):
        if self.left:
            yield from self.left.post_order_generator()
        if self.right:
            yield from self.right.post_order_generator()
        yield self.data


if __name__ == '__main__':

    root = Node('F')

    for v in 'BADCEGIH':
        root.insert(v)

    # Without generator:
    print(root.inorder())
    print(root.pre_order())
    print(root.post_order())

    # With generator:
    for i in root.inorder_generator():
        print(i)
    for i in root.pre_order_generator():
        print(i)
    for i in root.post_order_generator():
        print(i)
