import random
from meta_board import MetaBoard
from players import Player, _ASCII_REPRESENTATIONS



"""
This class represents the game itself, so it has a singluar 
MetaBoard and keeps track of who's turn it is.
It also handles the user's input  and updates the board accordingly
"""
class Game():
    # global variables for the size of the meta board and each single board:
    global _SIZE_META_BOARD
    _SIZE_META_BOARD = 3
    global _SIZE_SINGLE_BOARD
    _SIZE_SINGLE_BOARD = 3
    """
    Initialize the Game class
    :returns: nothing, updates state
    """
    def __init__(self):
        # set the first player to random
        first_player = random.randint(0, 1)
        self.current_player = Player(first_player)


        # make a meta game board, using the MetaBoard class
        self.game_board = MetaBoard(Player(0).name, Player(1).name, _ASCII_REPRESENTATIONS, _SIZE_META_BOARD, _SIZE_SINGLE_BOARD)

        # to keep track of if each player is a human or computer
        self.player_identity_is_human = {}
        self.player_identity_is_human[Player(0).name] = True
        self.player_identity_is_human[Player(1).name] = True

        # if the player is a computer, it will select a random move
        # out of the possible moves left, represented by a list,
        # as if the computer is taking notes
        self.possible_moves = []
        for row in range(_SIZE_META_BOARD):
            for col in range(_SIZE_META_BOARD):
                for row_within_square in range(_SIZE_SINGLE_BOARD):
                    for col_within_square in range(_SIZE_SINGLE_BOARD):
                        self.possible_moves.append((row, col, row_within_square, col_within_square))


    

    """
    prints an intro message to the game
    :returns: nothing
    """
    def intro_message(self):
        print("Welcome to Super Tic Tac Toe")
        print("This is a two player game on a mega meta tic tac toe board")
        print("The megaboard is composed of " + str(_SIZE_META_BOARD*_SIZE_META_BOARD) + "individual tic tac toe boards")
        print("You can play on anyone of them at anytime")
        print("Using the normal rules of tic tac toe, when you win an individual board, you take that square in the meta board")
        print("The mega board follows normal tic tac toe rules as well, so the ultimate task is to win the mega board")
        print("Good luck!")
        print()

    

    """
    helper method to get input on player identity and update state accordingly
    :name: name of the player
    :returns: nothing, updates states
    """
    def choose_player(self, name):
        player_identity = input("Do you want " + name + " to be a human (h) or computer (c)? ")
        while player_identity != "h" and player_identity != "c":
            player_identity = input("The input must be h or c: ")
            print(player_identity)
        if player_identity == "c":
            self.player_identity_is_human[name] = False




    """
    Helper function for the initial text displayed to the user
    :base_string: a string that changes depending on what is desired from the user
    :range: what range the user's input should be within
    :returns: the initial input string
    """
    def initial_input_string(self, base_string, range):
        return "Please enter the " +  base_string + " the square you would like to play in, 0 - " + str(range)+ ": "
    
    """
    Helper function for re-entry text displayed to the user
    :base_string: a string that changes depending on what is desired from the user
    :range: what range the user's input should be within
    :returns: re-entry input string
    """
    def reenter_input_string(self, base_string, range):
        return "Reenter the " + base_string + " the square you would like to play in, 0 - " + str(range) + ": "

    """
    This is a helper function that takes some input texts and displays it to the 
    user, getting their response. Then it validates that response in two ways
    (1) check that the response is an integer
    (2) check that the response is in the correct range
    It will keep asking for input from the user until those conditions are satisfied
    :input_text: The text displayed to the user
    :range_of_index: the desired maximum of the user's input
    :returns: the validated input, in integer form
    """
    def validate_type_and_range(self, input_text, range_of_index):
        input_var = input(input_text)
        input_var_int = None
        while True:
            try:
                input_var_int = int(input_var)
            except ValueError:
                # will keep looping until input is an int
                input_var = input("This is not a number try again: ")
            else:
                # break infinite loop if we're in the correct range
                if input_var_int in range(range_of_index):
                    break
                else:
                    # get new input from the user
                    print("The entered value must be between 0 and " + str(range_of_index-1))
                    input_var = input("Reenter: ")

        return input_var_int
    

    """
    This is a function to validate the user's input in total. There are a few steps
    (1) Validate the type and the range of the row and column of the desired square
    (2) Validate that the square has not been won (otherwise a ValueError is thrown)
    (3) Validate the type and the range of the row and column within the desired square
    (4) Validate that the specific square is not taken, or else a value error is thrown

    unless all four steps are validated, the program will continue an infinite loop
    the fourth step will start the whole function over, since the user may want to 
    pick a new square all together

    :returns: nothing, updates state
    """
    def validate_user_input_and_update_position(self):
        # Step one: validate the type and the range of the input row and column
        initial_input_string_row = self.initial_input_string("row of", _SIZE_META_BOARD)
        initial_input_string_col = self.initial_input_string("column of", _SIZE_META_BOARD)
        row = self.validate_type_and_range(initial_input_string_row, _SIZE_META_BOARD)
        col = self.validate_type_and_range(initial_input_string_col, _SIZE_META_BOARD)

        # Step two: validate that the square has not been won
        while True:
            try:
                self.game_board.validate_index(row, col)
            except ValueError as e:
                print(e)
                reenter_input_string_row = self.reenter_input_string("row", _SIZE_META_BOARD)
                reenter_input_string_col = self.reenter_input_string("column", _SIZE_META_BOARD)
                row = self.validate_type_and_range(reenter_input_string_row, _SIZE_META_BOARD)
                col = self.validate_type_and_range(reenter_input_string_col, _SIZE_META_BOARD)
            else:
                break
        
        # Step three: validate the type and range of the row and column within the specificed square
        initial_input_string_row_in_square = self.initial_input_string("row within", _SIZE_SINGLE_BOARD)
        initial_input_string_col_in_square = self.initial_input_string("column within", _SIZE_SINGLE_BOARD)
        row_in_square = self.validate_type_and_range(initial_input_string_row_in_square, _SIZE_SINGLE_BOARD)
        col_in_square = self.validate_type_and_range(initial_input_string_col_in_square, _SIZE_SINGLE_BOARD)

        # Step four: try to play at the desired spot, if it has not been taken
        try:
            self.game_board.play_turn(row, col, row_in_square, col_in_square, self.current_player.name)
        except ValueError as e:
            # if the spot has been taken, then start the input process over again
            print(e)
            self.validate_user_input_and_update_position()
        else:
            # once a move is made, remove it from the possible moves list for the computer
            self.possible_moves.remove((row, col, row_in_square, col_in_square))
                 
    """
    This is a function that plays as a computer
    It first chooses a random move out of the available move remaining
    Then it checks to see if the square in question has not been won yet
        if so it then updates the possible moves list according
        and keeps generating new random moves until a valid one is picked
    Once a valid move is picked, it is removed from possible moves
    :returns: nothing, updates state
    """
    def computer_plays(self):
        print("The computer plays")
        (row, col, row_in_square, col_in_square) = random.choice(self.possible_moves)
        while(True):
            try:
                self.game_board.validate_index(row, col)
            except ValueError:
                for row_within_square in range(_SIZE_SINGLE_BOARD):
                    for col_within_square in range(_SIZE_SINGLE_BOARD):
                        if (row, col, row_within_square, col_within_square) in self.possible_moves:
                            self.possible_moves.remove((row, col, row_within_square, col_within_square))
                (row, col, row_in_square, col_in_square) = random.choice(list(self.possible_moves))
            else:
                self.game_board.play_turn(row, col, row_in_square, col_in_square, self.current_player.name)
                self.possible_moves.remove((row, col, row_in_square, col_in_square))
                print("The computer plays on row: " + str(row) + ", and col: " + str(col))
                print("And within that square, the computer plays on row: " + str(row_in_square) +  ", and col: " + str(col_in_square))
                break


    """
    A singular game loop, which first prints the game board
    And tells the player who's turn it is
    Then it validates the user input and changes the state
    Then it changes the turn of the player


    :returns: nothing, updates state
    """
    def game_loop(self):
        print(self.game_board)
        print("Player " + self.current_player.name + "'s turn")
        if self.player_identity_is_human[self.current_player.name]:
            self.validate_user_input_and_update_position()
        else:
            self.computer_plays()


        self.current_player = Player((self.current_player.value + 1)%2)
    
    """
    plays the game, calling the single game loop method
    and repeating it until there is a winner
    :returns: nothing, updates state
    """
    def play_game(self):
        self.intro_message()
        self.choose_player(Player(0).name)
        self.choose_player(Player(1).name)
        while not (self.game_board.is_game_won() or self.game_board.is_game_tie()):
            self.game_loop()
        if (self.game_board.is_game_won()):
            print(self.game_board.game_winner() + " wins!")
        else:
            print("It's a tie!")
        print("Final game board:")
        print(self.game_board)
              
if __name__ == '__main__':
    game = Game()
    game.play_game()
