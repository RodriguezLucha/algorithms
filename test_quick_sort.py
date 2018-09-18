#!/usr/bin/env python


def partition(A, low, up):
    i = low + 1
    j = up
    pivot = A[low]
    while (i <= j):
        while (A[i] < pivot and i < up):
            i = i + 1
        while (A[j] > pivot):
            j = j - 1
        if (i < j):
            A[i], A[j] = A[j], A[i]
            i = i + 1
            j = j - 1
        else:
            i = i + 1
    A[low] = A[j]
    A[j] = pivot
    return j


def quick(A, low, up):
    if (low >= up):
        return
    piv_loc = partition(A, low, up)
    quick(A, low, piv_loc - 1)
    quick(A, piv_loc + 1, up)


def test_quick_sort():
    actual = [1, 0, 4, 8, 2, 7, 6, 5, 3]
    expected = sorted(actual)
    quick(actual, 0, len(actual) - 1)
    assert actual == expected


def test_quick_sort_1():
    actual = [1]
    expected = sorted(actual)
    quick(actual, 0, len(actual) - 1)
    assert actual == expected


def test_quick_sort_2():
    actual = []
    expected = sorted(actual)
    quick(actual, 0, len(actual) - 1)
    assert actual == expected


def test_quick_sort_3():
    actual = [1, -1, 3, 5, 9, -38]
    expected = sorted(actual)
    quick(actual, 0, len(actual) - 1)
    assert actual == expected


def test_quick_sort_4():
    actual = [1, 1, 1, 1, 1]
    expected = sorted(actual)
    quick(actual, 0, len(actual) - 1)
    assert actual == expected


def test_quick_sort_5():
    actual = [-10, -9, -7]
    expected = sorted(actual)
    quick(actual, 0, len(actual) - 1)
    assert actual == expected


def test_quick_sort_6():
    actual = [1, 2, 3]
    expected = sorted(actual)
    quick(actual, 0, len(actual) - 1)
    assert actual == expected
