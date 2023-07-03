# Sudoku Solver

This Python script allows you to read a Sudoku puzzle from a file or download it from an API and solves it using backtracking algorithm. It utilizes the `requests` library as an external dependency to fetch Sudoku puzzles from an API.

## Prerequisites

- Python 3.x
- `requests` library (can be installed via `pip install requests`)

## Usage

1. Clone the repository or download the Python script.

2. Install the required dependencies using the following command:
   ```
   pip install requests
   ```

3. Run the script using the following command:
   ```
   python sudoku_solver.py
   ```

## How to Use

### 1. Reading a Sudoku from a File

To solve a Sudoku puzzle from a file, follow these steps:

1. Create a text file containing the Sudoku puzzle. Use the following format:
   - Each line represents a row in the puzzle.
   - Use the numbers 1-9 to represent filled cells.
   - Use dots (.) or zeros (0) to represent empty cells.

   Example:
   ```
   5 3 . . 7 . . . .
   6 . . 1 9 5 . . .
   . 9 8 . . . . 6 .
   8 . . . 6 . . . 3
   4 . . 8 . 3 . . 1
   7 . . . 2 . . . 6
   . 6 . . . . 2 8 .
   . . . 4 1 9 . . 5
   . . . . 8 . . 7 9
   ```

2. Update the `filename` variable in the script with the path to your Sudoku puzzle file.

3. Run the script, and it will solve the Sudoku puzzle.

### 2. Downloading from dosuku API

if no path is provided, than a sukodu will automatically be downloaded from the dosuku API.

## Algorithm

The script implements a backtracking algorithm to solve the Sudoku puzzle. It uses a recursive approach to find the solution:

1. Find the first empty cell in the puzzle (marked with a dot or zero).
2. Try each number from 1 to 9 in that cell.
3. If a number is valid for the current cell (i.e., it doesn't violate any Sudoku rules), move to the next empty cell and repeat steps 2-3.
4. If all numbers have been tried for a cell, backtrack to the previous cell and try the next number.
5. Repeat steps 1-4 until the puzzle is solved.

The backtracking algorithm ensures that every possibility is explored until a solution is found.

## License

This project is licensed under the [MIT License](LICENSE).