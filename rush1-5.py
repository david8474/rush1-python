import sys

def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for i in range(y):
        for j in range(x):
            if x == 1 or y == 1:
                print("B", end="")
            elif i == 0 and j == 0:
                print("A", end="")
            elif i == 0 and j == x - 1:
                print("C", end="")
            elif i == y - 1 and j == 0:
                print("C", end="")
            elif i == y - 1 and j == x - 1:
                print("A", end="")
            elif i == 0 or i == y - 1 or j == 0 or j == x - 1:
                print("B", end="")
            else:
                print(" ", end="")
        print()
