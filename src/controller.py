"""Module containing the Controller class."""
from view import TextView, WebView
from puzzle import Puzzle
from solver import solve, solve_complete, hint_by_depth


class Controller:
    """Class responsible for connection between puzzles and views.

    You may add new *private* attributes to this class to help you
    in your implementation.
    """
    # === Private Attributes ===
    # @type _puzzle: Puzzle
    #     The puzzle associated with this game controller
    # @type _view: View
    #     The view associated with this game controller

    def __init__(self, puzzle, mode='text'):
        """Create a new controller.

        <mode> is either 'text' or 'web', representing the type of view
        to use.ss

        By default, <mode> has a value of 'text'.

        @type puzzle: Puzzle
        @type mode: str
        @rtype: None
        """
        self._puzzle = puzzle
        if mode == 'text':
            self._view = TextView(self)
        elif mode == 'web':
            self._view = WebView(self)
        else:
            raise ValueError()

        # Start the game.
        self._view.run()

    def state(self):
        """Return a string representation of the current puzzle state.

        @type self: Controller
        @rtype: str
        """
        return str(self._puzzle)

    def act(self, action):
        """Run an action represented by string <action>.

        Return a string representing either the new state or an error message,
        and whether the program should end.

        @type self: Controller
        @type action: str
        @rtype: (str, bool)
        """
        # TODO: Add to this method to handle different actions.
        if action == 'exit':
            return '', True
        elif action == "solve":
            return str(solve(self._puzzle)),True
        elif action == "solve-all":
            solution = solve_complete(self._puzzle)
            solution = list(map(lambda x: str(x), solution))
            return "\n".join(solution),True
        elif "hint" in action:
            if action[5].isdigit() and int(action[5]) >= 1:
                return str(hint_by_depth(self._puzzle,int(action[5]))),False
            else:
                return "Please enter input again!"
        elif self._puzzle.check(action) == ValueError:
            return "Incorrect input", False
        elif self._puzzle.check(action):
            return self._puzzle.move(action), True
        else:
            return self.state(), False



    def tree(self, puzzle, move):
        pass




if __name__ == '__main__':
    from sudoku_puzzle import SudokuPuzzle
    from word_ladder_puzzle import WordLadderPuzzle
    s = SudokuPuzzle([['', '', '', ''],
                      ['', '', '', ''],
                      ['C', 'D', 'A', 'B'],
                      ['A', 'B', 'C', 'D']])
    c = Controller(s)
