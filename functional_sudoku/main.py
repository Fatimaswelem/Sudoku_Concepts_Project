# Entry point that loads the puzzle into an immutable structure and prints the recursive solution to the console.

import os
from immutable_grid import Board, load_board_from_file
from recursive_solver import solve


# Pretty Print (Recursive)

def print_board(board: Board) -> None:
    _print_row(board, 0)

def _print_row(board: Board, r: int):
    if r == 9:
        return
    if r != 0 and r % 3 == 0:
        print("-" * 21)
    _print_cell(board, r, 0)
    print()
    _print_row(board, r + 1)

def _print_cell(board: Board, r: int, c: int):
    if c == 9:
        return
    if c != 0 and c % 3 == 0:
        print("| ", end="")
    val = board[r][c] if board[r][c] != 0 else "."
    print(val, end=" ")
    _print_cell(board, r, c + 1)

# Entry Point

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(base_dir, "../puzzles/puzzle2.txt")  # external file with puzzle
    initial_board: Board = load_board_from_file(filename)

    print("Original Sudoku Board:")
    print_board(initial_board)

    print("\nSolving...\n")
    solution = solve(initial_board)

    print("Solved Sudoku Board:")
    if solution:
        print_board(solution)
    else:
        print("No solution found.")
