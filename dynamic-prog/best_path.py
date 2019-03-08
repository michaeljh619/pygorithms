'''
TODO: Write explanation to problem
'''


class BestPath:
    def __init__(self, grid):
        # grid vals
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        # memoized grids
        self.score_grid = self.__create_empty_grid()
        self.path_grid = self.__create_empty_grid()

    def solve(self):
        # start at top left and tabulate grid
        for x in range(self.cols):
            for y in range(self.rows):
                # neighbor positions
                top_x = x
                top_y = y - 1
                left_x = x - 1
                left_y = y

                # value of current cell
                val = self.__get_item_from_grid(self.grid, x, y)

                # best scores from neighbors
                top_score = self.__get_item_from_grid(self.score_grid,
                                                      top_x, top_y)
                left_score = self.__get_item_from_grid(self.score_grid,
                                                       left_x, left_y)

                # best paths from neighbors
                top_path = self.__get_item_from_grid(self.path_grid,
                                                     top_x, top_y)
                left_path = self.__get_item_from_grid(self.path_grid,
                                                      left_x, left_y)

                # calculate best path and best score to this position
                best_path = ""
                best_score = val

                # determine which prev neighbor to use
                use_left_neighbor = False
                use_top_neighbor = False
                # top left position, no prev neighbors
                if top_score is None and left_score is None:
                    pass
                # on top edge
                elif top_score is None:
                    use_left_neighbor = True
                # on left edge
                elif left_score is None:
                    use_top_neighbor = True
                # two prev neighbors, pick which is better
                else:
                    if left_score > top_score:
                        use_left_neighbor = True
                    else:
                        use_top_neighbor = True

                # get best path and score based on which was better
                if use_left_neighbor:
                    best_path = left_path + "R"
                    best_score = left_score + val
                elif use_top_neighbor:
                    best_path = top_path + "D"
                    best_score = top_score + val

                # set best path and score
                self.score_grid[y][x] = best_score
                self.path_grid[y][x] = best_path

    def get_best_score(self):
        if self.rows == 0 or self.cols == 0:
            return 0
        return self.score_grid[self.rows-1][self.cols-1]

    def get_best_path(self):
        if self.rows == 0 or self.cols == 0:
            return ""
        return self.path_grid[self.rows-1][self.cols-1]

    def __create_empty_grid(self):
        new_grid = []
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                row.append(None)
            new_grid.append(row)
        return new_grid

    def __get_item_from_grid(self, grid, col, row):
        # determine if out of bounds
        if col < 0 or row < 0:
            return None
        if col >= len(grid[0]) or row >= len(grid):
            return None

        # get item
        return grid[row][col]
