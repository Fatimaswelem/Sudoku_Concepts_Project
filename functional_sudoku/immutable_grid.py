# Provides pure helper functions to parse files into read-only tuples and format output without side effects.
from typing import Tuple, Optional

# Board Type
Board = Tuple[Tuple[int, ...], ...]  # 9x9 immutable board

# Immutable Board Operations

def find_empty(board: Board) -> Optional[Tuple[int, int]]:
    """Find the first empty cell (0) in the board."""
    return _find_empty_recursive(board, 0, 0)

def _find_empty_recursive(board: Board, row: int, col: int) -> Optional[Tuple[int, int]]:
    if row == 9:
        return None
    if col == 9:
        return _find_empty_recursive(board, row + 1, 0)
    if board[row][col] == 0:
        return (row, col)
    return _find_empty_recursive(board, row, col + 1)

def set_cell(board: Board, row: int, col: int, val: int) -> Board:
    """Return a new board with value set at (row, col)."""
    return _set_row(board, row, col, val, 0)

def _set_row(board: Board, row: int, col: int, val: int, r: int) -> Board:
    if r == 9:
        return ()
    return (_set_cell(board, row, col, val, r, 0),) + _set_row(board, row, col, val, r + 1)

def _set_cell(board: Board, row: int, col: int, val: int, r: int, c: int) -> Tuple[int, ...]:
    if c == 9:
        return ()
    new_val = val if (r == row and c == col) else board[r][c]
    return (new_val,) + _set_cell(board, row, col, val, r, c + 1)

# Load Board from External File

def load_board_from_file(filename: str) -> Board:
    """
    Load a Sudoku puzzle from a file into an immutable Board.
    File format: 9 lines, 9 numbers each (0 = empty), separated by spaces.
    """
    with open(filename, "r") as f:
        lines = f.read().strip().splitlines()
    if len(lines) != 9:
        raise ValueError("Puzzle must have exactly 9 lines")
    board = tuple(
        tuple(int(x) for x in line.split())
        for line in lines
    )
    if any(len(row) != 9 for row in board):
        raise ValueError("Each row must have exactly 9 numbers")
    return board
