import sys
from loader import from_sudoku_api, from_txt


def show_grid(grid):
    print("-" * 37)
    for i, row in enumerate(grid):
        print(
            ("|" + " {}   {}   {} |" * 3).format(*[x if x != 0 else " " for x in row])
        )
        if i == 8:
            print("-" * 37)
        elif i % 3 == 2:
            print("|" + "---+" * 8 + "---|")
        else:
            print("|" + "   +" * 8 + "   |")


def guess(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num:
            return False

    for i in range(9):
        if grid[i][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True


def solve_sudoku(grid, row, col):
    if row == len(grid) - 1 and col == len(grid):
        return True
    if col == len(grid):
        row += 1
        col = 0
    if grid[row][col] > 0:
        return solve_sudoku(grid, row, col + 1)
    for num in range(1, len(grid) + 1):
        if guess(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False


def main():
    args = sys.argv[1:]
    if not args:
        grid = from_sudoku_api()
    else:
        grid = from_txt(args[0])
    print("ORIGINAL:")
    show_grid(grid)
    if solve_sudoku(grid, 0, 0):
        print("SOLUTION:")
        show_grid(grid)
    else:
        print("Solution does not exist:(")


if __name__ == "__main__":
    main()
