# Entry point that initializes the Pygame GUI and manages the main application loop using mutable state.

import pygame
import sys
import os
from state import SudokuGrid
from gui import SudokuGUI  # We will create this file next!

# --- Configuration ---
WINDOW_WIDTH = 540
WINDOW_HEIGHT = 600
FPS = 60

def main():
    # 1. Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Sudoku - Imperative Version")
    clock = pygame.time.Clock()

    # 2. Initialize the Mutable State (The Grid)
    game_state = SudokuGrid()
    
    # Construct path to the shared puzzle file
    # Note: We go up one level (..) then into 'puzzles'
    puzzle_path = os.path.join("..", "puzzles", "puzzle1.txt")
    
    # Load the puzzle (Modifies game_state in place)
    game_state.load_from_file(puzzle_path)

    # 3. Initialize the GUI Renderer
    # We pass the screen so the GUI knows where to draw
    ui = SudokuGUI(screen)

    # 4. The Imperative Game Loop
    # This is the definition of imperative: "While this is true, do this..."
    running = True
    while running:
        # A. Event Handling (Check for inputs)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # (Future: Add mouse clicks here to select cells)

        # B. Update State
        # (Future: logic.solve_step() would go here for the AI)

        # C. Draw to Screen
        screen.fill((255, 255, 255))  # Clear screen with White
        
        # We ask the GUI to draw the current state of the board
        current_board = game_state.get_board()
        ui.draw_board(current_board)
        
        # D. Refresh Display
        pygame.display.flip()
        clock.tick(FPS)

    # Cleanup
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()