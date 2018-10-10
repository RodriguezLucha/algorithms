#!/usr/bin/env python


class Solution():

    def __init__(self):
        self.sols = []
        self.subs = []

    def is_solution(self):
        if len(self.nums) == len(self.sols):
            return True
        else:
            return False

    def get_candidates(self):
        if len(self.sols) < len(self.nums):
            return [True, False]
        else:
            return []

    def add_to_solution(self):
        subset = []
        for sol, num in zip(self.sols, self.nums):
            if sol:
                subset.append(num)
        self.subs.append(subset)

    def backtrack(self):
        if self.is_solution():
            self.add_to_solution()
        possible = self.get_candidates()
        for p in possible:
            self.sols.append(p)
            self.backtrack()
            self.sols.pop()

    def subsets(self, nums):
        self.nums = nums
        self.backtrack()
        return self.subs


def test_basic():
    s = Solution()

    nums = [1, 2, 3]
    expected = [[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []]
    actual = s.subsets(nums)
    assert checkEqual(actual, expected)


def checkEqual(L1, L2):
    return len(L1) == len(L2) and sorted(L1) == sorted(L2)
