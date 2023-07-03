import os
from shutil import ExecError
import requests


def from_sudoku_api() -> list[list[int]]:
    response = requests.get("https://sudoku-api.vercel.app/api/dosuku")
    sudoku = response.json()["newboard"]["grids"][0]["value"]
    return sudoku


def from_txt(path: str) -> list[list[int]]:
    valid_chars = "1234567890."
    if not os.path.exists(path):
        raise Exception("File not found.")

    with open(path, "r") as f:
        str_grid = f.readlines()
    grid = []
    for line in str_grid:
        line = line.rstrip()
        if not all([c if c in valid_chars else None for c in line.split(" ")]):
            raise Exception("File is not properly formatted.")
        line = [int(n) if n != "." else 0 for n in line.split(" ")]
        grid.append(line)
    return grid


from_txt("src/data/sudoku.txt")
