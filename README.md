Rush1 Python – ASCII Pattern Generator
📌 Overview

This project implements multiple variations of an ASCII pattern generator using Python.
Each function generates rectangular patterns with different border styles based on input dimensions.

The goal is to demonstrate:

Control flow (loops and conditions)
Clean logic design
Handling edge cases (e.g., width/height = 1)
🧠 Features
Generate patterns with customizable width (x) and height (y)
Multiple pattern styles (rush1-2 to rush1-5)
Handles edge cases (single row/column)
Simple and efficient logic
📂 Project Structure
rush1-python/
├── rush1-2.py
├── rush1-3.py
├── rush1-4.py
├── rush1-5.py
▶️ Usage

Run any file with:

python rush1-3.py x y
Example:
python rush1-3.py 5 3

Output:

ABBBA
B   B
CBBBC
⚙️ How It Works

Each script:

Iterates through rows (y) and columns (x)
Applies conditions to determine:
Corners
Borders
Interior spaces
Prints the pattern directly to the console
🚀 Skills Demonstrated
Python fundamentals
Nested loops
Conditional logic
Problem-solving and pattern design
Clean code structure
📈 Future Improvements
Convert to a single modular program
Add CLI argument validation
Support additional pattern styles
Export output to files
