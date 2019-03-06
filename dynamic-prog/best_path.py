class BestPath:
    def __init__(self, grid):
        # grid vals
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        # memoized grids
        self.score_grid = self.__create_empty_grid()
        self.path_grid = self.__create_empty_grid()

    def tabulate(self):
        pass

    def __create_empty_grid(self):
        new_grid = []
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                row.append(None)
            new_grid.append(row)
        return new_grid
