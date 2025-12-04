import os
from immutable_grid import Board, load_board_from_file
from recursive_solver import solve

# ---------- PURE BOARD STRING FUNCTIONS ----------
def board_to_string(board: Board) -> str:
    return _rows_to_string(board, 0)

def _rows_to_string(board: Board, r: int) -> str:
    if r == 9:
        return ""
    line = ""
    if r != 0 and r % 3 == 0:
        line += "-" * 21 + "\n"
    line += _cells_to_string(board, r, 0) + "\n"
    return line + _rows_to_string(board, r + 1)

def _cells_to_string(board: Board, r: int, c: int) -> str:
    if c == 9:
        return ""
    prefix = "| " if c != 0 and c % 3 == 0 else ""
    val = board[r][c] if board[r][c] != 0 else "."
    return prefix + str(val) + " " + _cells_to_string(board, r, c + 1)

# ---------- ENTRY POINT ----------
if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(base_dir, "../puzzles/puzzle2.txt")
    initial_board: Board = load_board_from_file(filename)

    print("Original Sudoku Board:")
    print(board_to_string(initial_board))

    print("\nSolving...\n")
    solution = solve(initial_board)

    print("Solved Sudoku Board:")
    if solution:
        print(board_to_string(solution))
    else:
        print("No solution found.")
