"""
Aufgabe:

Create a simple decision tree composed of binary attributes for a game of your choice and write a program
to evaluate it based on the values of the attributes concerned.

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


def visible_audible_10mAway_flank(S):
    assert len(S) == 4
    root = Node(S[0])
    root.left = Node(S[1])
    root.right = Node
    root.right = Node

if __name__ == '__main__':
    #1101
    root = Node(0)
    root.left = Node(1)
    root.left.left = Node('Creep')
    root.right = Node
