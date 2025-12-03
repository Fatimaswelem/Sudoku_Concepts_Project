# Entry point that initializes the Pygame GUI and manages the main application loop using mutable state.

import pygame
import sys
import os
from state import SudokuGrid
from gui import SudokuGUI 
from logic import SudokuSolver

# --- Configuration ---
WINDOW_WIDTH = 540
WINDOW_HEIGHT = 600
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Sudoku - Imperative AI Solver")
    clock = pygame.time.Clock()

    # 1. Initialize State
    game_state = SudokuGrid()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    puzzle_path = os.path.join(current_dir, "..", "puzzles", "puzzle1.txt")
    
    if os.path.exists(puzzle_path):
        game_state.load_from_file(puzzle_path)
    else:
        print(f"Warning: Puzzle file not found at {puzzle_path}")

    # 2. Initialize GUI
    ui = SudokuGUI(screen)

    # 3. Initialize Solver
    solver = SudokuSolver(game_state, ui)

    print("AI Ready. Press SPACE to watch the solver run.")

    running = True
    solved = False

    while running:
        # A. Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # TRIGGER: One button to start the AI
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not solved:
                    print("Starting Solver...")
                    solver.solve()
                    solved = True
                    print("Solved!")

        # B. Draw to Screen
        ui.update(game_state)
        
        # C. Refresh Display
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main() 