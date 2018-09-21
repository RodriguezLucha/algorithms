from pprint import pprint


class Cell():

    def __init__(self):
        self.cost = 0
        self.parent = 0


class Solution():

    MATCH = 0
    INSERT = 1
    DELETE = 2

    def __init__(self, beg, end):
        self.table = []

        self.s = beg
        self.t = end

        self.rows = len(beg) + 1
        self.cols = len(end) + 1

        for row in range(self.rows):
            new_row = []
            for col in range(self.cols):
                new_row.append(Cell())
            self.table.append(new_row)

    def row_init(self, i):

        self.table[0][i].cost = i

        if (i > 0):
            self.table[0][i].parent = Solution.INSERT
        else:
            self.table[0][i].parent = -1

        return

    def col_init(self, i):

        self.table[i][0].cost = i

        if (i > 0):
            self.table[i][0].parent = Solution.DELETE
        else:
            self.table[i][0].parent = -1

        return

    def match(self, c, d):
        if c == d:
            return 0
        else:
            return 1

    def indel(self, c):
        return 1

    def string_compare(self):

        s = self.s
        t = self.t
        m = self.table
        opt = [None, None, None]

        for i in range(self.cols):
            self.row_init(i)

        for i in range(self.rows):
            self.col_init(i)

        for i in range(1, len(self.s) + 1):
            for j in range(1, len(self.t) + 1):
                opt[Solution.MATCH] = m[i - 1][j - 1].cost + self.match(
                    s[i - 1], t[j - 1])
                opt[Solution.INSERT] = m[i][j - 1].cost + self.indel(t[j - 1])
                opt[Solution.DELETE] = m[i - 1][j].cost + self.indel(s[i - 1])

                m[i][j].cost = opt[Solution.MATCH]
                m[i][j].parent = Solution.MATCH

                k = Solution.INSERT

                while k <= Solution.DELETE:
                    if opt[k] < m[i][j].cost:
                        m[i][j].cost = opt[k]
                        m[i][j].parent = k
                    k += 1

        self.print_cost()

    def print_cost(self):
        table_str = ""

        for row in range(self.rows):
            table_str += "["
            table_str += ",".join(
                [str(x.cost).rjust(5) for x in self.table[row]])
            table_str += "]\n"

        print(table_str)
        return

    def print_parent(self):

        table_str = ""

        for row in range(self.rows):
            table_str += "["
            table_str += ",".join(
                [str(x.parent).rjust(5) for x in self.table[row]])
            table_str += "]\n"

        print(table_str)

        return


def test_edit_distance():

    print ""
    beg = "you should not"
    end = "thou shalt not"
    # beg = "123"
    # end = "1234"
    s = Solution(beg, end)
    actual = s.string_compare()
    expected = 5
    return actual == expected
