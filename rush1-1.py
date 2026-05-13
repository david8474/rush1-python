import sys

def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for i in range(y):
        for j in range(x):
            if (i == 0 or i == y - 1) and (j == 0 or j == x - 1):
                print("o", end="")
            elif i == 0 or i == y - 1:
                print("-", end="")
            elif j == 0 or j == x - 1:
                print("|", end="")
            else:
                print(" ", end="")
        print()

