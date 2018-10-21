#!/usr/bin/env python
import pytest


class Node():

    def __init__(self, value):
        self.value = value
        self.children = []
        self.term = False


class Trie():

    def __init__(self, words):
        self.root = None
        self.__make(words)

    def __make(self, words):

        root = Node(None)

        for word in words:
            current = root

            for letter in list(word):

                for child in current.children:
                    if child.value == letter:
                        current = child
                        break

                node = Node(letter)
                current.children.append(node)
                current = node

            current.term = True

        self.root = root
        return

    def search(self, word):
        current = self.root
        total = len(word)
        matched = 0
        for letter in list(word):
            for child in current.children:
                if letter == child.value:
                    matched += 1
                    if matched == total and child.term == True:
                        return True
                    current = child
                    break

        return False


@pytest.fixture()
def words():
    return [
        "vacation",
        "valley",
        "valuable",
        "variety",
        "vast",
        "version",
        "victim",
        "video",
        "view",
        "violence",
    ]


def test_trie(words):
    trie = Trie(words)
    assert trie.search("vacation") == True
    assert trie.search("vacatio") == False
    assert trie.search("videographer") == False
    assert trie.search("vim") == False
