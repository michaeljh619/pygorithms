from breadth_first_search import BreadthFirstSearch
from depth_first_search import DepthFirstSearch
from dijkstra import Dijkstra
from digraph import DirectedGraph as DG
from digraph import Vertex
import pytest


def pytest_generate_tests(metafunc):
    # types of searches
    search_types = [BreadthFirstSearch, DepthFirstSearch]
    shortest_search_types = [Dijkstra]

    # parametrize general searches
    if 'searcher' in metafunc.fixturenames:
        metafunc.parametrize('searcher', search_types)

    # types of shortest searches
    if 'shortest_searcher' in metafunc.fixturenames:
        metafunc.parametrize('shortest_searcher', shortest_search_types)

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
    graph_start_end_shortestpath = [
        (DG([[1, 3], [3, 2], [1, 2]]), 1, 2, [1, 2]),
        (DG([[1, 3], [3, 7], [7, 4], [4, 2], [1, 5], [5, 2]]),
         1, 2, [1, 5, 2]),
        (DG([[1, 3, 1], [3, 2, 2], [1, 2, 2]]), 1, 2, [1, 2]),
        (DG([[1, 3], [3, 7], [7, 4], [4, 2], [1, 5], [5, 2, 4]]),
         1, 2, [1, 3, 7, 4, 2]),
    ]

    # parametrize simple search
    if 'graph_start_end_path' in metafunc.fixturenames:
        metafunc.parametrize('graph_start_end_path',
                             graph_start_end_path)

    # parametrize shortest path search
    if 'graph_start_end_shortestpath' in metafunc.fixturenames:
        metafunc.parametrize('graph_start_end_shortestpath',
                             graph_start_end_path +
                             graph_start_end_shortestpath)


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


def test_shortest_search(shortest_searcher,
                         graph_start_end_shortestpath):
    # get all vars from param
    g = graph_start_end_shortestpath[0]
    start = graph_start_end_shortestpath[1]
    end = graph_start_end_shortestpath[2]
    correct_path = graph_start_end_shortestpath[3]

    # search
    output_path = shortest_searcher.search(g, start, end)

    # check that they match
    assert output_path == correct_path
