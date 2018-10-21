#!/usr/bin/env python
from graph import Graph, Node
import sys
from collections import defaultdict


def dijkstra_search(graph, start, end):
    parents = defaultdict(str)
    distances = defaultdict(lambda: sys.maxint)

    distances[start] = 0

    seen = set()

    a = start
    while (len(seen) < len(graph.edges)):
        seen.add(a)
        for node in graph.edges[a]:
            b = node.val
            w = node.weight

            if (distances[a] + w) < distances[b]:
                distances[b] = distances[a] + w
                parents[b] = a

        dist = sys.maxint
        unseen = set(graph.edges.keys()).difference(seen)
        for val in unseen:
            if distances[val] < dist:
                dist = distances[val]
                a = val

    path = []
    p = end

    while p in parents:
        path.append(p)
        p = parents[p]

        if p == start:
            path.append(start)

    return list(reversed(path))


def test_call_dijkstra_basic():

    graph = Graph(directed=True)

    graph.read_graph("""
                     A B 2
                     A C 8
                     A D 5
                     B C 1
                     C E 3
                     D E 4
                     """)

    path = dijkstra_search(graph, start="A", end="E")
    expected = ["A", "B", "C", "E"]
    assert path == expected


def test_call_dijkstra_wikipedia():

    graph = Graph(directed=True)

    graph.read_graph("""
                     A B 4
                     A C 2
                     B C 5
                     B D 10
                     C E 3
                     D F 11
                     E D 4
                     """)

    path = dijkstra_search(graph, start="A", end="F")
    expected = ["A", "C", "E", "D", "F"]
    assert path == expected

