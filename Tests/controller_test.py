from soln.controller_soln import Controller
import sys
from io import StringIO


def run_controller(puzzle, commands, filename=''):
    """Simulate running the game on a given puzzle and set of commands.

    If a file name is specified, write output to that file.
    Otherwise, print to the screen.

    Precondition: <commands> must be a sequence of commands which causes
    the controller to terminate (e.g., by entering 'exit' or ':SOLVE').

    @type puzzle: Puzzle
    @type commands: list[str]
    @rtype: None
    """
    out = StringIO('')
    sys.stdout = out
    sys.stdin = StringIO('\n'.join(commands))
    Controller(puzzle)
    r = out.getvalue()
    out.close()
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__

    outputs = r.split('Enter a command:\n> ')
    messages = []
    for i in range(len(outputs)):
        messages.append(outputs[i])
        if i < len(commands):
            messages.append('Enter a command:\n> ')
            messages.append(commands[i] + '\n')

    if filename == '':
        print(''.join(messages))
    else:
        with open(filename, 'w') as result_file:
            result_file.writelines(messages)

if __name__ == '__main__':
    from soln.sudoku_puzzle_soln import SudokuPuzzle
    s = SudokuPuzzle([['A', 'B', 'C', 'D'],
                      ['C', 'D', 'A', 'B'],
                      ['B', 'A', '', ''],
                      ['D', 'C', '', '']])

    run_controller(s, ['(2, 2) -> D',
                       '(2, 3) -> D',  # Note: invalid move
                       ':UNDO',
                       '(2, 3) -> C',
                       ':UNDO',
                       ':ATTEMPTS',
                       ':SOLVE'],
                   'solved.txt')
