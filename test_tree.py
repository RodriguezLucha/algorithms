#!/usr/bin/env python
from binarytree import build


class Solution(object):

    def __init__(self):
        self.sym = True

    def traverse(self, n1, n2):
        if n1 == None and n2 == None:
            return
        else:
            if n1 == None or n2 == None or n1.value != n2.value:
                self.sym = False
                return
            self.traverse(n1.left, n2.right)
            self.traverse(n1.right, n2.left)

    def isSymmetric(self, root):
        self.traverse(root, root)
        return self.sym


def test_given_1():
    tree = build([1, 2, 2, 3, 4, 4, 3])
    #        __1__
    #       /     \
    #      2       2
    #     / \     / \
    #    3   4   4   3
    expected = True
    s = Solution()
    actual = s.isSymmetric(tree)
    assert actual == expected


def test_given_2():
    tree = build([1, 2, 2, None, 3, None, 3])
    #      __1
    #     /   \
    #    2     2
    #     \     \
    #      3     3
    expected = False
    s = Solution()
    actual = s.isSymmetric(tree)
    assert actual == expected
