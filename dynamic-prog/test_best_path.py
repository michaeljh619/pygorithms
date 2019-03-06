from best_path import BestPath

import pytest


def pytest_generate_tests(metafunc):
    grids = [
        [[]],
        [[1]],
        [[0, 2], [1, 0]],
        [[0, 2, 3], [1, 4, 0]]
    ]
    if 'grid' in metafunc.fixturenames:
        metafunc.parametrize('grid', grids)


def test_constructor(grid):
    # create best path object
    bp = BestPath(grid)
    assert bp.rows == len(grid)
    assert bp.cols == len(grid[0])


def test_create_empty_grid(grid):
    # create obj
    bp = BestPath(grid)
    empty_grid = bp._BestPath__create_empty_grid()
    assert len(empty_grid) == len(grid)
    assert len(empty_grid[0]) == len(grid[0])
