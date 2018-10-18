#!/usr/bin/env python


def get_permutations(s):
    if len(s) == 0:
        return [""]
    elif len(s) == 1:
        return [s]
    else:

        perms = []
        for i in range(len(s)):
            c = s[i]
            rem = s[:i] + s[i + 1:]

            for p in get_permutations(rem):
                perms.append(c + p)

        return perms


def test_permutations_basic():
    input_str = "ABC"
    expected = ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
    actual = get_permutations(input_str)
    assert actual == expected
