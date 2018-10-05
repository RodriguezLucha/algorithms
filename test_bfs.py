#!/usr/bin/env python


class Solution():

    class Point():

        def __init__(self, row, col):
            self.row = row
            self.col = col

        def __eq__(self, other):
            return self.col == other.col and self.row == other.row

        def __ne__(self, other):
            return self.col != other.col or self.row != other.row

    def in_image(self, point):

        num_rows = len(self.image)
        num_cols = len(self.image[0])

        if point.row >= 0 and point.row < num_rows:
            if point.col >= 0 and point.col < num_cols:
                return True

        return False

    def start_color_match(self, point):
        return self.image[point.row][point.col] == self.start_color

    def floodFill(self, image, sr, sc, newColor):

        self.start_color = image[sr][sc]
        self.image = image

        processed = []
        q = []
        start = self.Point(sr, sc)
        q.append(start)

        while (len(q) > 0):
            current = q.pop()

            if current in processed:
                continue

            processed.append(current)

            r = current.row
            c = current.col

            top = self.Point(r + 1, c)
            bottom = self.Point(r - 1, c)
            left = self.Point(r, c - 1)
            right = self.Point(r, c + 1)

            surrounding = [top, bottom, left, right]

            for point in surrounding:
                if self.in_image(point) and self.start_color_match(point):
                    q.append(point)

        for point in processed:
            image[point.row][point.col] = newColor

        return image


def test_basic_breadth_first_search_using_queue():
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    expected = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    s = Solution()
    actual = s.floodFill(image, sr, sc, newColor)
    assert expected == actual
