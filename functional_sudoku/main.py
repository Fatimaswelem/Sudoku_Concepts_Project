# Entry point that loads the puzzle into an immutable structure and prints the recursive solution to the console.



# Functional: Reads all lines at once and creates a frozen structure
with open('../puzzles/puzzle1.txt', 'r') as file:
    # Creates a tuple of tuples (immutable)
    grid = tuple(tuple(int(n) for n in line.split()) for line in file)
# Result: A read-only data structure. They must create NEW grids to solve it.