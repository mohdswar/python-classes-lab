# In this lab, you can practice object-oriented programming (OOP) by building a Tic-tac-toe terminal game with Python Classes.

# While working through this lab, consider the gameplay of Tic-Tac-Toe and, if necessary, pseudocode it. Try to write several small functions, each performing a single purpose, e.g., print_board, get_move, check_for_winner, etc. Consider how/where looping makes sense, e.g., loop until the player enters a correct move or until the game's over, etc.

# User Stories
# Your goal is to implement the following user stores:

# As a user (AAU), I want to see a welcome message at the start of a game.
# AAU, before being prompted for a move, I want to see the board printed in the console to know what moves have been made.
# AAU, at the beginning of each turn, told whose turn it is: It's player X's turn!
# AAU, I should be prompted to enter a move and be provided an example of valid input ('Enter a valid move (example: A1)').
# AAU, I want to be able to enter my move's column letter in upper or lower case (a/A, b/B, or c/C) to make it easier to enter my move.
# AAU, if I enter a move in an invalid format or try to occupy a cell already taken, I want to see a message chastising me and be re-prompted.
# AAU, after entering a move, I should once again be presented with the updated game board, notified of the current turn, and asked to enter a move for the other player. This process should continue until there is a winner or a tie
# AAU, I should see a message at the end of the game indicating the winner or stating that the game ended in a tie.
class Game():
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None  # Corrected this line
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def play_game(self):
        print("Welcome to Tic Tac Toe!")

    def print_board(self):
        b = self.board
        print(f"""
        A   B   C
    1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
        ----------
    2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
        ----------
    3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
  """)

    def print_message(self):
        if self.tie:
            print("It's a tie!")
        if self.winner:
            print(f"{self.winner} wins!")
        else:
            print(f"It's {self.turn}'s turn!")

    def get_move(self):
        while True:
            move = input(f"Enter a valid move (example: A1): ").lower()
            if move in self.board and not self.board[move]:
                self.board[move] = self.turn
                return move
            else:
                print("Invalid move. Please try again.")

    def check_for_winner(self):
        win_stat = [
            ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],
            ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],
            ['a1', 'b2', 'c3'], ['a3', 'b2', 'c1']
        ]
        # checks if all values have all x or o
        for condition in win_stat:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] and self.board[condition[0]] is not None:
                self.winner = self.turn
                return

    def check_for_tie(self):
        if None not in self.board.values() and self.winner is None:
            self.tie = True

    def switch_turn(self):
        if self.turn == "X":
            self.turn = 'O'
        elif self.turn == 'O':
            self.turn = 'X'

    def play_game(self):
        print("Shall we play a game?")
        while not self.winner and not self.tie:
            self.print_board()
            self.print_message()
            self.get_move()
            self.check_for_winner()
            self.check_for_tie()
            if not self.winner and not self.tie:
                self.switch_turn()
        self.print_board()
        self.print_message()

game_instance = Game()
game_instance.play_game()