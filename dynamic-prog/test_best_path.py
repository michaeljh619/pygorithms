from best_path import BestPath

import pytest


def pytest_generate_tests(metafunc):
    grids = [
        [[]],
        [[1]],
        [[0, 2], [1, 0]],
        [[0, 2, 3], [1, 4, 0]],
        [[0, 2, 3], [1, 4, 0], [5, 12, 0]],
    ]
    if 'grid' in metafunc.fixturenames:
        metafunc.parametrize('grid', grids)

    grid_score_paths = [
        (grids[0], 0, ""),
        (grids[1], 1, ""),
        (grids[2], 2, "RD"),
        (grids[3], 6, "RDR"),
        (grids[4], 18, "RDDR"),
    ]
    if 'grid_score_path' in metafunc.fixturenames:
        metafunc.parametrize('grid_score_path', grid_score_paths)


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


def test_get_item_from_grid(grid):
    # create obj
    bp = BestPath(grid)

    # loop from -1 to 1 over end of length of grid
    for col in range(-1, len(grid)+1):
        for row in range(-1, len(grid[0])+1):
            # getting item from outside of grid
            should_be_none = False
            if col < 0 or col >= len(grid[0]):
                should_be_none = True
            elif row < 0 or row >= len(grid):
                should_be_none = True

            if should_be_none:
                assert bp._BestPath__get_item_from_grid(grid,
                                                        col,
                                                        row) is None
            else:
                assert bp._BestPath__get_item_from_grid(grid,
                                                        col,
                                                        row) == grid[row][col]


def test_solution(grid_score_path):
    grid = grid_score_path[0]
    score = grid_score_path[1]
    path = grid_score_path[2]

    bp = BestPath(grid)
    bp.solve()

    assert bp.get_best_score() == score
    assert bp.get_best_path() == path
