from breadth_first_search import BreadthFirstSearch
from depth_first_search import DepthFirstSearch
from digraph import DirectedGraph as DG
from digraph import Vertex
import pytest


def pytest_generate_tests(metafunc):
    # types of searches
    search_types = [BreadthFirstSearch, DepthFirstSearch]
    if 'searcher' in metafunc.fixturenames:
        metafunc.parametrize('searcher', search_types)

    # sample graphs
    graph_start_end_path = [
        (DG([[1, 1]]), 1, 2, None),
        (DG([[1, 1]]), 1, 1, [1]),
        (DG([[1, 2]]), 1, 2, [1, 2]),
        (DG([[1, 3], [3, 2]]), 1, 2, [1, 3, 2]),
        (DG([[1, 3], [3, 2], [1, 5], [3, 7]]), 1, 2, [1, 3, 2]),
        (DG([[1, 3], [3, 2], [1, 5], [3, 7],
             [3, 3], [3, 1], [2, 12], [2, 1]]), 1, 2, [1, 3, 2])
    ]
    if 'graph_start_end_path' in metafunc.fixturenames:
        metafunc.parametrize('graph_start_end_path',
                             graph_start_end_path)


def test_search_matches_given_path(searcher, graph_start_end_path):
    # get all vars from param
    g = graph_start_end_path[0]
    start = graph_start_end_path[1]
    end = graph_start_end_path[2]
    correct_path = graph_start_end_path[3]

    # search
    output_path = searcher.search(g, start, end)

    # check that they match
    assert output_path == correct_path
