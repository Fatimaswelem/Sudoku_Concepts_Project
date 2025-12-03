# Implements the backtracking algorithm using iterative loops (for/while) to update the board in place.
import pygame

class SudokuSolver:
    def __init__(self, grid_object, gui_object):
        self.grid_obj = grid_object
        self.gui = gui_object 
        self.board = grid_object.get_board()

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
        Solves the board using Backtracking with VISUALIZATION.
        """
        find = self.find_empty()
        if not find:
            return True # Solved
        
        row, col = find

        for i in range(1, 10):
            if self.is_valid(row, col, i):
                # 1. Mutate State
                self.grid_obj.update_cell(row, col, i)
                
                # 2. VISUALIZE: Update the screen immediately!
                self.gui.update(self.grid_obj)
                # pygame.time.delay(50) # Optional: Uncomment to slow it down (AI is very fast!)

                # 3. Recursive Step
                if self.solve():
                    return True

                # 4. Backtrack (Mutate State back to 0)
                self.grid_obj.update_cell(row, col, 0)
                self.gui.update(self.grid_obj) # Visualize the backtrack removal

        return False

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0: return (i, j)
        return None