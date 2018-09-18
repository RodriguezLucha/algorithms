from collections import defaultdict


class Node():

    def __init__(self, val, weight):
        self.val = val
        self.weight = weight


class Graph():

    def __init__(self, directed):
        self.edges = {}
        self.degrees = defaultdict(int)
        self.directed = directed

    def read_graph(self, graph_str):
        graph_str = graph_str.strip()
        lines = graph_str.split("\n")
        lines = [l.strip() for l in lines]
        for line in lines:
            f = line.split(" ")
            a = f[0]
            b = f[1]
            w = int(f[2])
            self.insert_edge(a, b, w)

        return True

    def insert_edge(self, a, b, w):

        if a not in self.edges:
            self.edges[a] = []
        if b not in self.edges:
            self.edges[b] = []

        node = Node(val=b, weight=w)
        self.edges[a].append(node)
        self.degrees[a] += 1

        if not self.directed:
            node = Node(val=a, weight=w)
            self.edges[b].append(node)
            self.degrees[b] += 1

    def print_graph(self):
        """
        A:['B(2)', 'C(8)', 'D(5)']
        B:['C(1)']
        C:['E(3)']
        D:['E(4)']
        """
        print ""
        for a in sorted(self.edges.keys()):
            print "{}:{}".format(
                a, ["{}({})".format(n.val, n.weight) for n in self.edges[a]])
