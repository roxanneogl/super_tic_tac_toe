
from single_board import SingleBoard

"""
This class utilizes the singleBoard class and stores a 2D array
of singleBoards to represent the multi game board
It also contains a tracker, in the form of a singleBoard to represnt
the whole metagame. This is updated when a single board is won
"""
class MetaBoard:

    """
    Initialize the metaBoard class
    :player_one_string: string representing player one
    :player_two_string: string represting player two
    :ascii dictionary: a dictionary with ascii representations of the players
    :size_meta_board: size of one dimension of the meta board, assumed to be square
        defaulted to 3
    :size_board: size of one dimension of each singular board, assumed to be square
        defaulted to 3
    :returns: nothing, updates state
    """
    def __init__(self, player_one_string, player_two_string, ascii_dictionary, size_meta_board = 3, size_single_board = 3):
        self.size_meta_board = size_meta_board 
        self.size_single_board = size_single_board

        # 2day array of boards representing the whole game board
        self.boards = [[SingleBoard(player_one_string, player_two_string, ascii_dictionary, self.size_single_board) for i in range(self.size_meta_board)] for j in range(self.size_meta_board)]

        # this is single board to keep track of who has won each square and what that implies for the overall game
        self.meta_board_tracker = SingleBoard(player_one_string, player_two_string, ascii_dictionary, size_meta_board)
    
    """
    String representation of the class
    :returns: a string that looks like the meta tic tac toe board
    """
    def __str__(self):
        returnString = ""
        for row in self.boards:
            # since each board are each represented as multi-line strings,
            # to put them side by side for each row we have to put them into arrays
            lines = [str(sing_board).splitlines() for sing_board in row]
            # put the right line of each board side by side
            for i in range(len(lines[0])):
                returnString += "|"
                for line in lines:
                    returnString += line[i]
                    returnString += "|"
                returnString += "\n"
            returnString += "-" * ((len(lines[0]) + 4) * len(lines))
            returnString += "\n"
        return returnString
    
    """
    Helper function for simplicity
    :returns: if the the game is won
    """
    def is_game_won(self):
        return self.meta_board_tracker.square_won
    
    """
    Helper function for simplicity
    :returns: who the winner of the game is
    """
    def game_winner(self):
        return self.meta_board_tracker.winner
    
    """
    Helper function for simplicity
    :returns: if the game is a tie
    """
    def is_game_tie(self):
        isFull = True
        # check to see if the game boards are full
        for row in self.boards:
            for board in row:
                if not(board.is_tie()) and not(board.square_won):
                    isFull = False
        return self.meta_board_tracker.is_tie() or isFull
    
    """
    Play a singular turn and update the state
    :row: the row of the square to be updated
    :column: the column of the square to be updated
    :row_in_square: the row to be updated within the chosen square
    :column_in_square: the column to be updated within the chosen square
    :player_name: the player who's turn it is
    :returns: nothing, updates state
    """
    def play_turn(self, row, column, row_in_square, column_in_square, player_name):
        square_chosen = self.boards[row][column]
        square_chosen.play_square(row_in_square, column_in_square, player_name)
        if square_chosen.square_won:
            # update the metaboard once the square has been won
            self.meta_board_tracker.play_square(row, column, player_name)
    
    """
    Before the row and the column within a specific square are chosen,
    we want to validate the row and column of the square itself
    to make sure the square has not been run
    :row: the row we are checking
    :column: the column we are checking
    :returns: nothing
    :raises: ValueError if the square has been won
    """
    def validate_index(self, row, column):
        if self.boards[row][column].square_won:
            raise ValueError("This square has already been won.")

    



        

