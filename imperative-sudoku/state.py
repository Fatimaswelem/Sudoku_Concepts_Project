# Defines the mutable Grid class that maintains the board state using a modifiable 2D list.

import os
import copy

class SudokuGrid:
    def __init__(self):
        # Initialize a BLANK 9x9 grid of zeros
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        # Keep track of which numbers were "givens" (clues)
        self.original_grid = [[0 for _ in range(9)] for _ in range(9)]

    def load_from_file(self, filename):
        """Reads the file imperatively and sets the internal state."""
        new_grid = []
        
        if not os.path.exists(filename):
            print(f"Error: File {filename} not found!")
            return

        with open(filename, 'r') as file:
            for line in file:
                '''---HIGHER ORDER IMPLEMENTATION--- (makes code not 100% Imperative)
                # Instead of a loop or list comprehension, we use map().
                # map() takes a function (int) and applies it to every item in the list.'''
                # COMMENTED BC IT TAKES WAY TOO LONG TO EXCUTE (~2 MINUTES ON MY MACHINE)
                row = list(map(int, line.split()))

                # ---IMPERATIVE IMPLEMENTATION---
                #row = [int(num) for num in line.split()]

                new_grid.append(row)
        
        # Update state
        self.grid = new_grid
        self.original_grid = copy.deepcopy(new_grid)
        
        print(f"Puzzle loaded! Grid size: {len(self.grid)}x{len(self.grid[0])}")

    def get_board(self):
        """Returns the current state of the board."""
        return self.grid

    def is_original(self, row, col):
        """Returns True if the cell was a starting clue."""
        return self.original_grid[row][col] != 0

    def update_cell(self, row, col, value):
        """Mutates a specific cell in the grid."""
        self.grid[row][col] = value