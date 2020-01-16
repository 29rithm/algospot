from copy import deepcopy


def minimumHours(rows, columns, grid):
    min_hours = 0
    while True:

        all_deployed = True
        for r in range(rows):
            for c in range(columns):
                this = grid[r][c]
                if this==0:
                    all_deployed = False
        if all_deployed:
            break

        new_grid = deepcopy(grid)
        for r in range(rows):
            for c in range(columns):

                this = grid[r][c]

                if this == 0:
                    continue

                if 0 <= c - 1:
                    new_grid[r][c-1] = 1
                if c + 1 < columns:
                    new_grid[r][c+1] = 1
                if 0 <= r - 1:
                    new_grid[r-1][c] = 1
                if r + 1 < rows:
                    new_grid[r+1][c] = 1
        grid = new_grid
        # for i in range(len(grid)):
        #     print(grid[i])
        # print()

        min_hours += 1

    return min_hours


if __name__ == '__main__':
    grid = [
        [0, 1, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0]
    ]
    print(minimumHours(4, 5, grid))
