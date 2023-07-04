#!/usr/bin/python3

"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chesschess.

Usage:
    ./101-nqueens.py N

Where N must be a number greater or equal to 4.
"""

import sys


def init_chess(n):
    """Initialize an `n x n` sized chesschess with 0's."""
    chess = []
    [chess.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in chess]
    return (chess)


def chess_deepcopy(chess):
    """Return a deepcopy of a chesschess."""
    if isinstance(chess, list):
        return list(map(chess_deepcopy, chess))
    return (chess)


def get_solution(chess):
    """
    Return the list of lists representation of a solved chesschess
    """
    solution = []
    for r in range(len(chess)):
        for c in range(len(chess)):
            if chess[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def xout(chess, row, col):
    """X out spots on a chesschess.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    :param chess: The current working chesschess.
    :type chess: list
    :param row: The current row to place a queen.
    :type row: int
    :param col: The current column to place a queen.
    :type col: int
    """
    # X out all forward spots
    for c in range(col + 1, len(chess)):
        chess[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        chess[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(chess)):
        chess[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        chess[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(chess)):
        if c >= len(chess):
            break
        chess[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chess[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(chess):
            break
        chess[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(chess)):
        if c < 0:
            break
        chess[r][c] = "x"
        c -= 1


def recursive_solve(chess, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    :param chess: The current working chesschess.
    :type chess: list
    :param row: The current row to place a queen.
    :type row: int
    :param queens: The number of queens placed on the chess.
    :type queens: int
    :param solutions: A list of solutions.
    :type solutions: list
    """
    if queens == len(chess):
        solutions.append(get_solution(chess))
        return (solutions)

    for c in range(len(chess)):
        if chess[row][c] == " ":
            tmp_chess = chess_deepcopy(chess)
            tmp_chess[row][c] = "Q"
            xout(tmp_chess, row, c)
            solutions = recursive_solve(tmp_chess, row + 1,
                                        queens + 1, solutions)

    return (solutions)


def validate_args():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        return False
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        return False
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        return False
    return True


if __name__ == "__main__":
    if not validate_args():
        sys.exit(1)

    chess = init_chess(int(sys.argv[1]))
    solutions = recursive_solve(chess, 0, 0, [])
    for sol in solutions:
        print(sol)
