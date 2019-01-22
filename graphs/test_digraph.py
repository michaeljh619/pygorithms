# import digraph
from digraph import DirectedGraph as DG
from digraph import Vertex
# import pytest
import pytest

def pytest_generate_tests(metafunc):
    # adj list parameter
    adj_lists = [
        [],
        [ [0, 0] ],
        [ [0, 1] ],
        [ [0, 1], [1, 0] ],
        [ [0, 1], [3, 4], [1, 2], [2, 3] ],
        [ [0,1], [0,2], [1,2], [2,0], [2,3], [3,3] ]
    ]
    if 'adj_list' in metafunc.fixturenames:
        metafunc.parametrize('adj_list', adj_lists)

def test_num_vertices(adj_list):
    # create graph
    g = DG(adj_list)

    # count all unique id's in adj_list
    s = set()
    for a in adj_list:
        s.add(a[0])
        s.add(a[1])

    # vertices and set length match
    assert len(g.vertices) == len(s)

def test_num_connections(adj_list):
    # create graph
    g = DG(adj_list)

    # count num connections
    num_connections = 0
    for v in g.vertices:
        num_connections += len(v.neighbors)

    # compare
    assert len(adj_list) == num_connections

def test_connections(adj_list):
    # create graph
    g = DG(adj_list)

    # test each connection
    for a in adj_list:
        # get vertices
        v0 = g.get_vertex(a[0])
        v1 = g.get_vertex(a[1])
        # ensure connection exists
        v_neighbor = v0.get_neighbor(a[1])
        assert v_neighbor != None
        # ensure connection is to v1
        assert v1 == v_neighbor
