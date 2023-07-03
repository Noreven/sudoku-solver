import requests


def from_sudoku_api() -> list[list[int]]:
    response = requests.get("https://sudoku-api.vercel.app/api/dosuku")
    sudoku = response.json()["newboard"]["grids"][0]["value"]
    return sudoku


def from_txt(path: str) -> list[list[int]]:
    pass
