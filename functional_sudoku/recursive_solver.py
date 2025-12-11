# Implements the solver using pure recursion, passing new board copies instead of modifying variables.

from typing import Optional
from immutable_grid import Board, find_empty, set_cell
from typing import Callable

# Validity Checks

def is_valid(board: Board, row: int, col: int, val: int) -> bool:
    return (_valid_row(board, row, val, 0) and
            _valid_col(board, col, val, 0) and
            _valid_block(board, row, col, val))

def _valid_row(board: Board, row: int, val: int, c: int) -> bool:
    if c == 9:
        return True
    if board[row][c] == val:
        return False
    return _valid_row(board, row, val, c + 1)

def _valid_col(board: Board, col: int, val: int, r: int) -> bool:
    if r == 9:
        return True
    if board[r][col] == val:
        return False
    return _valid_col(board, col, val, r + 1)


# Higher order function to check 3x3 block using recursion

def check_block_recursive(row: int, col: int, fn: Callable[[int, int], bool]) -> bool:
    """Check 3x3 block for validity."""
    start_r, start_c = 3 * (row // 3), 3 * (col // 3)

    def check(r: int, c: int) -> bool:
        if r == start_r + 3:
            return True
        if c == start_c + 3:
            return check(r + 1, start_c)
        if not fn(r, c):
            return False
        return check(r, c + 1)

    return check(start_r, start_c)

def _valid_block(board, row, col, val):
    return check_block_recursive(row, col, lambda r, c: board[r][c] != val) #high ordering line


# Recursive Sudoku Solver

def solve(board: Board) -> Optional[Board]:
    """Solve the Sudoku board. Returns a solved board or None."""
    empty = find_empty(board)
    if empty is None:
        return board
    row, col = empty
    return _try_values(board, row, col, 1)

def _try_values(board: Board, row: int, col: int, val: int) -> Optional[Board]:
    if val == 10:
        return None
    if is_valid(board, row, col, val):
        new_board = set_cell(board, row, col, val)
        solved = solve(new_board)
        if solved is not None:
            return solved
    return _try_values(board, row, col, val + 1)
