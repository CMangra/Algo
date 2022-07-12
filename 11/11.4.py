"""
Aufgabe:

Create a simple decision tree composed of binary attributes for a game of your choice and write a program
to evaluate it based on the values of the attributes concerned.

@Chaitanya
Kommentare:
Der Entscheidungsbaum, den ich hier implememtiert habe, ist aus dem Skript, Seite 392.

Folgende Methode implementiert:
visible_audible_10mAway_flank(S):   S ist eine Liste und kann nur vier Elemente haben, die entweder 0 oder 1 sind.
                                    1. Element: visible, 2. Element: audible, usw...
                                    links ist 0/No, recht ist 1/Yes
def parse_tree(root):               Gibt Creep, Attack, Move oder Do nothing zurück

"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def visible_audible_10mAway_flank(S):
    assert len(S) == 4
    root = Node(S[0])
    root.left = Node(S[1])

    root.left.right = Node('Creep')
    root.left.left = Node('Do nothing')

    root.right = Node(S[2])
    root.right.right = Node('Attack')

    root.right.left = Node(S[3])
    root.right.left.left = Node('Attack')
    root.right.left.right = Node('Move')
    return root


def parse_tree(root):
    if root.data == 1:
        parse_tree(root.right)
    elif root.data == 0:
        parse_tree(root.left)
    else:
        print(root.data)


if __name__ == '__main__':
    S = [1, 0, 0, 1]
    root = visible_audible_10mAway_flank(S)
    parse_tree(root)
