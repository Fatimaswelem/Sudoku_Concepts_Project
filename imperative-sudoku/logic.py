# Implements the backtracking algorithm using iterative loops (for/while) to update the board in place.
import pygame

class SudokuSolver:
    def __init__(self, grid_object, gui_object):
        self.grid_obj = grid_object
        self.gui = gui_object 
        self.board = grid_object.get_board()
        self.steps = 0 # NEW: Counter to track attempts

    def is_valid(self, row, col, num):
        """Checks if placing 'num' is valid using ITERATION."""
        # Check Row
        for x in range(9):
            if self.board[row][x] == num: return False
        # Check Column
        for x in range(9):
            if self.board[x][col] == num: return False
        # Check Box
        start_row, start_col = (row // 3) * 3, (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num: return False
        return True

    def solve(self):
        """
        Solves the board using Backtracking with OPTIMIZED VISUALIZATION.
        """
        find = self.find_empty()
        if not find:
            return True # Solved
        
        row, col = find

        for i in range(1, 10):
            if self.is_valid(row, col, i):
                # 1. Mutate State
                self.grid_obj.update_cell(row, col, i)
                
                # 2. VISUALIZE: Update screen every 50 steps only!
                self.steps += 1
                if self.steps % 50 == 0: 
                    self.gui.update(self.grid_obj)
                    pygame.event.pump() # Keeps window from freezing on Mac

                # 3. Recursive Step
                if self.solve():
                    return True

                # 4. Backtrack
                self.grid_obj.update_cell(row, col, 0)
                
                # OPTIONAL: Visualizing backtracks makes it look cooler but slower.
                # Uncomment the next two lines if you want to see deletions too.
                if self.steps % 50 == 0:
                    self.gui.update(self.grid_obj)

        return False

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0: return (i, j)
        return None