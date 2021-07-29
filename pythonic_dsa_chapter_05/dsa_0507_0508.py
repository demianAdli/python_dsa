class GameEntry:
    """Represents one entry of a list of high scores."""

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)   # e.g., (Bob, 98)


class Scoreboard:
    """Fixed-length sequence of high scores in nondecreasing order."""

    def __init__(self, capacity=10):
        """Initialize scoreboard with given maximum capacity.

        All entries are initially None.
        """
        self._board = [None] * capacity     # reserve space for future scores
        self._n = 0             # number of actual entries

    def getitem (self, k):
        """Return entry at index k."""
        return self._board[k]

    def __str__(self):
        """Return string representation of the high score list."""
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        """Consider adding entry to high scores."""
        score = entry.get_score()

        # Does new entry qualify as a high score?
        # answer is yes if board not full or score is higher than last entry
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):      # no score drops from list
                self._n += 1                    # so overall number increases

            # shift lower scores rightward to make room for new entry
            j = self._n - 1
            while j > 0 and self._board[j - 1].get_score() < score:
                self._board[j] = self._board[j - 1]   # shift entry from j-1 to j
                j -= 1      # and decrement j
            self._board[j] = entry  # when done, add new entry


if __name__ == "__main__":
    scoreboard_1 = Scoreboard()
    player_1 = GameEntry("Ali", 0)
    player_2 = GameEntry("Sara", 5)
    player_3 = GameEntry("Arash", 10)
    player_7 = GameEntry("Sam", 20)
    player_4 = GameEntry("Quentin", 11)
    player_5 = GameEntry("David", 21)
    player_6 = GameEntry("Ned", 3)
    player_8 = GameEntry("Luci", 12)
    player_9 = GameEntry("Kate", 12)
    player_10 = GameEntry("Lili", 25)
    player_11 = GameEntry("Demian", 1)
    player_12 = GameEntry("Audry", 25)
    scoreboard_1.add(player_7)
    scoreboard_1.add(player_1)
    scoreboard_1.add(player_2)
    scoreboard_1.add(player_3)
    scoreboard_1.add(player_4)
    scoreboard_1.add(player_5)
    scoreboard_1.add(player_10)
    scoreboard_1.add(player_6)
    scoreboard_1.add(player_8)
    scoreboard_1.add(player_9)
    scoreboard_1.add(player_10)
    # scoreboard_1.record(player_11)
    scoreboard_1.add(player_12)

    print(scoreboard_1)