# Defines the mutable Grid class that maintains the board state using a modifiable 2D list

import os

class SudokuGrid:
    def __init__(self):
        # Initialize an empty list (Mutable State)
        self.grid = []

    def load_from_file(self, filename):
        """
        Reads the file imperatively and sets the internal state.
        """
        # Reset the grid to ensure it's empty before loading
        self.grid = []
        
        # YOUR SNIPPET GOES HERE
        # We verify the file exists first to avoid crashing
        if not os.path.exists(filename):
            print(f"Error: File {filename} not found!")
            return

        with open(filename, 'r') as file:
            for line in file:
                # Loop through each line, convert to int, and append to the state
                row = [int(num) for num in line.split()]
                self.grid.append(row)
        
        print(f"Puzzle loaded! Grid size: {len(self.grid)}x{len(self.grid[0])}")

    def get_board(self):
        """Returns the current state of the board."""
        return self.grid

    def update_cell(self, row, col, value):
        """
        Mutates a specific cell in the grid.
        This is the definition of 'Imperative' - changing memory in place.
        """
        self.grid[row][col] = value