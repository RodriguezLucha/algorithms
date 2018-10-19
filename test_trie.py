#!/usr/bin/env python


class Node():

    def __init__(self, value):
        self.value = value
        self.children = []
        self.term = False


def get_words():
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


def make_trie(words):

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

    return root


def search_trie(word, root):
    current = root
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


def test_trie_found():
    word = "vacation"
    root = make_trie(get_words())
    actual = search_trie(word, root)
    expected = True
    assert actual == expected


def test_trie_not_found_almost():
    word = "vacatio"
    root = make_trie(get_words())
    actual = search_trie(word, root)
    expected = False
    assert actual == expected


def test_trie_not_found_longer_word():
    word = "videographer"
    root = make_trie(get_words())
    actual = search_trie(word, root)
    expected = False
    assert actual == expected


def test_trie_not_small_word():
    word = "vim"
    root = make_trie(get_words())
    actual = search_trie(word, root)
    expected = False
    assert actual == expected
