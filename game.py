from meta_board import meta_board
from players import Player, _ASCII_REPRESENTATIONS
import random


"""
This class represents the game itself, so it has a singluar 
MetaBoard and keeps track of who's turn it is.
It also handles the user's input  and updates the board accordingly
"""
class game():
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
        self.current_player = Player(0)

        # make a meta game board, using the MetaBoard class
        self.game_board = meta_board(Player(0).name, Player(1).name, _ASCII_REPRESENTATIONS, _SIZE_META_BOARD, _SIZE_SINGLE_BOARD)
    

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
            self.validate_user_input()
                 

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
        self.validate_user_input_and_update_position()
        self.current_player = Player((self.current_player.value + 1)%2)
    
    """
    plays the game, calling the single game loop method
    and repeating it until there is a winner
    :returns: nothing, updates state
    """
    def play_game(self):
        while not self.game_board.is_game_won():
            self.game_loop()
        print(self.game_board.game_winner() + " wins!")
        print("Final game board:")
        print(self.game_board)
              
game().play_game()
