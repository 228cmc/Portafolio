
# SudokuSolver

This project implements a Sudoku-solving agent using classical AI techniques, specifically backtracking search with constraint checking. It is capable of solving Sudoku puzzles of varying difficulty, while also rejecting invalid or unsolvable inputs.

Originally developed as part of the CM50270 Reinforcement Learning module at the University of Bath.

## Project Structure

```
SudokuSolver/
│
├── data/                  # Contains Sudoku puzzles and their solutions (.npy)
├── images/                # Contains reference images (e.g., sudoku.png)
├── venv/                  # Python virtual environment (optional)
├── sudoku.ipynb           # Main Jupyter notebook: implementation and evaluation
├── requirements.txt       # Python dependencies
├── Report.pdf             # Accompanying report (for submission)
├── README.md              # Project overview (this file)
└── .gitignore             # Git exclusions
```

## Problem Description

A Sudoku puzzle is a 9x9 grid where some digits (1–9) are already filled in. The goal is to fill the remaining empty cells (represented as 0s) so that:

- Each row contains the digits 1 to 9 without repetition.
- Each column contains the digits 1 to 9 without repetition.
- Each of the 3x3 subgrids contains the digits 1 to 9 without repetition.

The agent must return a valid solution if one exists, and return an array filled with -1 if the puzzle is invalid or unsolvable.

## Features

- Implements the `sudoku_solver()` function used for automatic evaluation.
- Validates puzzles before solving.
- Solves puzzles using backtracking and constraint propagation.
- Rejects invalid or unsolvable Sudoku puzzles.
- Includes tests for multiple difficulty levels: very easy, easy, medium, hard.
- Final check script ensures notebook is ready for submission.

## How to Run

1. Clone the repository or download the project folder.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Open the notebook:

   ```bash
   jupyter notebook sudoku.ipynb
   ```

4. Set `SKIP_TESTS = False` in the relevant cell to evaluate your implementation across all puzzles.
5. Restore `SKIP_TESTS = True` before final submission.

## Evaluation

The solver is automatically evaluated using:

- Accuracy on puzzles of increasing difficulty.
- Ability to reject invalid inputs.
- Performance (time taken per puzzle).

The notebook includes a final submission check to verify:

- Correct function name and output format.
- Proper file naming and presence of required files.

## Report

The file `Report.pdf` provides additional context on:

- Algorithm selection and implementation.
- Design decisions and challenges.
- Performance observations and conclusions.

## Notes

- The puzzle files (`.npy`) are structured as arrays with shape (15, 9, 9).

```
