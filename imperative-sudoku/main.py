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
    
    # --- FIX: USE ABSOLUTE PATHS ---
    # This finds the exact folder where main.py lives
    base_folder = os.path.dirname(os.path.abspath(__file__))
    # This goes up one level to 'Sudoku_Concepts_Project', then down to 'puzzles'
    puzzle_path = os.path.join(base_folder, "..", "puzzles", "puzzle2.txt")
    
    # Debug print to show you exactly where it is looking
    print(f"Looking for puzzle at: {puzzle_path}")

    if os.path.exists(puzzle_path):
        game_state.load_from_file(puzzle_path)
    else:
        print(f"CRITICAL ERROR: Puzzle file not found at {puzzle_path}")
        print("Please check that your folder structure is: Sudoku_Concepts_Project/puzzles/puzzle1.txt")

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