"""Word ladder module.

Rules of Word Ladder
--------------------
1. You are given a start word and a target word (all words in this puzzle
   are lowercase).
2. Your goal is to reach the target word by making a series of *legal moves*,
   beginning from the start word.
3. A legal move at the current word is to change ONE letter to get
   a current new word, where the new word must be a valid English word.

The sequence of words from the start to the target is called
a "word ladder," hence the name of the puzzle.

Example:
    Start word: 'make'
    Target word: 'cure'
    Solution:
        make
        bake
        bare
        care
        cure
"""
from puzzle import Puzzle


CHARS = 'abcdefghijklmnopqrstuvwyz'


class WordLadderPuzzle(Puzzle):
    """A word ladder puzzle."""
    # TODO: add to this list of private attributes!
    # === Private attributes ===
    # @type _words: list[str]
    #

    def __init__(self, start, target):
        """Create a new word ladder puzzle with given start and target words.

        Note: you may add OPTIONAL arguments to this constructor,
        but you may not change the purpose of <start> and <target>.

        @type self: WordLadderPuzzle
        @type start: str
        @type target: str
        @rtype: None
        """
        # Code to initialize _words - you don't need to change this.
        self._words = []
        with open('wordsEnTest.txt') as wordfile:
            for line in wordfile:
                self._words.append(line.strip())

        # TODO: Complete the constructor.
        self._ladder = [start]
        self._currentWord = self._ladder[0]
        self._target = target

    def __str__(self):
        ladder = ''
        for word in reversed(self._ladder):
            ladder += word + "\n"
        return ladder

    def is_solved(self):
        return self._currentWord == self._target

    def extensions(self):
        """Return a list of possible new states after a valid move.

        The valid move must change exactly one character of the
        current word, and must result in an English word stored in
        self._words.

        You should *not* perform any moves which produce a word
        that is already in the ladder.

        The returned moves should be sorted in alphabetical order
        of the produced word.

        @type self: WordLadderPuzzle
        @rtype: list[WordLadderPuzzle]
        """
        moves = []
        for i in range(len(self._currentWord)):
            for letter in CHARS:
                word = self._currentWord[:i] + letter + self._currentWord[i+1:]
                if word in self._words and word not in self._ladder:
                    moves.append(word)

        moves = sorted(moves)
        for i in range(len(moves)):
            moves[i] = WordLadderPuzzle(moves[i],self._target)
            moves[i]._ladder.reverse
            moves[i]._ladder.extend(self._ladder)
            moves[i]._ladder.reverse

        return moves

    def check(self, move):
        if len(move) > len(self._ladder[0]):
            raise ValueError
        changed = 0
        for i, q in zip(move, self._currentWord):
            if i != q:
                changed += 1
            else:
                pass
        if changed > 1 or move not in self._words:
            raise ValueError
        else:
            return True


    def move(self, move):
        self._ladder.append(move)
        self._currentWord = move
        word_latter = WordLadderPuzzle(self._currentWord, self._target)
        word_latter._ladder = self._ladder
        word_latter._currentWord = self._currentWord
        return word_latter


