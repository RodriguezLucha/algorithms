#!/usr/bin/env python
from pprint import pprint
from graph import Graph, Node


def test_read_graph():
    graph = Graph(directed=True)
    graph.read_graph(sample_1())
    # graph.print_graph()


def sample_1():
    graph = """
            A B 2
            A C 8
            A D 5
            B C 1
            C E 3
            D E 4
            """
    return graph
