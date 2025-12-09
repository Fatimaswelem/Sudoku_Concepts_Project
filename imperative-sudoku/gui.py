# Handles all Pygame rendering operations to draw the grid and visualize the imperative solution process.

import pygame

class SudokuGUI:
    def __init__(self, screen):
        self.screen = screen
        self.width = 540
        self.height = 600
        self.grid_height = 540
        self.cell_size = 540 // 9
        
        # Define Fonts & Colors
        self.font = pygame.font.SysFont("comicsans", 40)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255) # Color for AI moves

    def draw_board(self, grid_obj):
        """
        Draws the grid and numbers.
        """
        board = grid_obj.get_board()
        gap = self.cell_size
        
        # 1. Draw Grid Lines
        for i in range(10):
            thick = 4 if i % 3 == 0 else 1
            # Horizontal
            pygame.draw.line(self.screen, self.BLACK, (0, i * gap), (self.width, i * gap), thick)
            # Vertical
            pygame.draw.line(self.screen, self.BLACK, (i * gap, 0), (i * gap, self.grid_height), thick)

        # 2. Draw Numbers
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != 0:
                    # Color Logic: Black for Clues, Blue for AI
                    if grid_obj.is_original(i, j):
                        color = self.BLACK
                    else:
                        color = self.BLUE
                        
                    # Render text
                    text = self.font.render(str(val), 1, color)
                    
                    # Perfect Centering
                    cell_center_x = j * gap + gap / 2
                    cell_center_y = i * gap + gap / 2
                    text_rect = text.get_rect(center=(cell_center_x, cell_center_y))
                    
                    self.screen.blit(text, text_rect)
    
    def update(self, grid_obj):
        """Helper to redraw and refresh the screen instantly."""
        self.screen.fill(self.WHITE)
        self.draw_board(grid_obj)
        pygame.display.update()