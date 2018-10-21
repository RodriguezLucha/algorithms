#!/usr/bin/env python
import pytest


def partition(A, low, up):
    i = low + 1
    j = up
    pivot = A[low]
    while (i <= j):
        while (A[i] < pivot and i < up):
            i += 1
        while (A[j] > pivot):
            j -= 1
        if (i < j):
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        else:
            i += 1
    A[low] = A[j]
    A[j] = pivot
    return j


def quick(A, low, up):
    if (low >= up):
        return
    piv_loc = partition(A, low, up)
    quick(A, low, piv_loc - 1)
    quick(A, piv_loc + 1, up)


a = []
a.append([1, 0, 4, 8, 2, 7, 6, 5, 3])
a.append([1])
a.append([])
a.append([1, 1, 1, 1, 1])
a.append([-10, -9, -7])
a.append([1, -1, 3, 5, 9, -38])
a.append([1, 2, 3])


@pytest.mark.parametrize('A', a)
def test_quicksort(A):
    actual = A
    expected = sorted(actual)
    quick(actual, 0, len(actual) - 1)
    assert actual == expected
