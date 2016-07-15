"""This module contains functions responsible for solving a puzzle.

This module can be used to take a puzzle and generate one or all
possible solutions. It can also generate hints for a puzzle (see Part 4).
"""
from puzzle import Puzzle


def solve(puzzle, verbose=False):
    """Return a solution of the puzzle.

    Even if there is only one possible solution, just return one of them.
    If there are no possible solutions, return None.

    In 'verbose' mode, print out every state explored in addition to
    the final solution. By default 'verbose' mode is disabled.

    Uses a recursive algorithm to exhaustively try all possible
    sequences of moves (using the 'extensions' method of the Puzzle
    interface) until it finds a solution.

    @type puzzle: Puzzle
    @type verbose: bool
    @rtype: Puzzle | None
    """
    result = puzzle.extensions()
    if puzzle.is_solved():
        return puzzle
    elif result is []:
        return puzzle
    else:
        for i in result:
            if solve(i).is_solved():
              return solve(i)
        return puzzle

def solve_complete(puzzle, verbose=False):
    """Return all solutions of the puzzle.

    Return an empty list if there are no possible solutions.

    In 'verbose' mode, print out every state explored in addition to
    the final solution. By default 'verbose' mode is disabled.

    Uses a recursive algorithm to exhaustively try all possible
    sequences of moves (using the 'extensions' method of the Puzzle
    interface) until it finds all solutions.

    @type puzzle: Puzzle
    @type verbose: bool
    @rtype: list[Puzzle]
    """
    result = puzzle.extensions()
    for i in result:
        print(i)
    lst = []
    if puzzle.is_solved():
        return [puzzle]
    elif result is []:
        return 0
    else:
        for i in result:
            if solve_complete(i) != 0:
                lst.extend(solve_complete(i))

        return lst

def hint_by_depth(puzzle, n):
    """Return a hint for the given puzzle state.

    Precondition: n >= 1.

    If <puzzle > is already solved, return the string 'Already at a solution!'
    If <puzzle> cannot lead to a solution or other valid state within <n> moves,
    return the string 'No possible extensions!'

    @type puzzle: Puzzle
    @type n: int
    @rtype: str
    """
    lst = []
    moves = puzzle.extensions()
    if puzzle.is_solved():
        return "Already at a solution!"
    elif n == 1:
        if moves is []:
            return "No possible extensions!"
        else:
            for result in moves:
                if result.is_solved():
                    return True

            return moves[0]
    else:
        for i in moves:
            x = hint_by_depth(i, n-1)
            if x:
                return i
            elif x == i:
                return i





if __name__ == '__main__':
    from word_ladder_puzzle import WordLadderPuzzle
    from sudoku_puzzle import SudokuPuzzle


    s = WordLadderPuzzle("mare","mist")
    for i in s.extensions():
        print(i)
