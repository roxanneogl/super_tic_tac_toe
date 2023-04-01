"""
This class represents a single board of the meta tic tac toe game.
It has a 2d array to represent moves made and keeps track of if
the square has been won and by whom.
"""
class SingleBoard:


    """
    initialize the singleBoard class
    :player_one_string: string representing player one
    :player_two_string: string represting player two
    :ascii dictionary: a dictionary with ascii representations of the players
    :size_board: size of one dimension of the board, assumed to be square
        defaulted to 3
    :returns: nothing, updates state
    """
    def __init__(self, player_one_string, player_two_string, ascii_dictionary, size_board=3):
        self.ascii_dictionary = ascii_dictionary
        self.size_board = size_board

        # board is a representation of the tic tac toe grid, initialized to all empty
        self.board = [['-' for i in range(self.size_board)] for j in range(self.size_board)]

        """
        This variable is to keep track of the possible ways a person could win the square.
        It tallies the number of marks of a player for each column, row, and diagonal
        It is implemented this way to avoid looping through each square when checking
        for a win
        """
        self.win_check = {}
        self.initialize_checking_win_dictionary(player_one_string, player_two_string)

        # count to keep track of how many cells are full
        # so we can know if it's a tie when the board is full
        self.fill_count = 0

        # variables to keep track of it the game has been won and the winner
        self.square_won = False
        self.winner = None
    
    """
    string representation of the class
    :returns: a string that looks like a 2d tic tac toe board
    """
    def __str__(self):
        returnString = ""
        if self.square_won:
            return self.ascii_dictionary[self.winner]
        for row in self.board:
            for symbol in row:
                returnString += symbol
                returnString += " "
            returnString += "\n"
        return returnString

    """
    initializes our win dictionary
    :player_one_string: string representing player one
    :player_two_string: string represting player two
    :returns: nothing, updates state
    """
    def initialize_checking_win_dictionary(self, playerOneString, playerTwoString):
        # first we will make a list of all the keys for our dictionary
        # each key represents a possible way to win a square
        dictionary_keys = []
        for i in range(self.size_board):
            dictionary_keys.append(("column" + str(i), playerOneString)) 
            dictionary_keys.append(("row" + str(i), playerOneString))
            dictionary_keys.append(("column" + str(i), playerTwoString))
            dictionary_keys.append(("row" + str(i), playerTwoString))
        dictionary_keys.append(("diagonal_top_left", playerOneString)) 
        dictionary_keys.append(("diagonal_top_right", playerOneString)) 
        dictionary_keys.append(("diagonal_top_left", playerTwoString)) 
        dictionary_keys.append(("diagonal_top_right", playerTwoString))

        # then we make a dictionary from these keys, setting their value
        # to zero since no moves have been made
        self.win_check = dict.fromkeys(dictionary_keys, 0)


    """
    helper method to see if the square is full
    does not update state
    :param row: row to be checked
    :param column: column to be checked
    """
    def is_square_full(self, row, column):
        return self.board[row][column] != '-'


    """
    play_square method, updates the single board based on input
        row and column.
    :param row: row to be updated
    :param column: column to be updated
    :returns: nothing, updates state
    :raises a value error, if the cell is taken
    """
    def play_square(self, row, column, player_name):
        # all tests where an error is raised are theoretically
        # checked at a higher level, but there is additional 
        # error raised for safe-guarding
        if row not in range(self.size_board ):
            raise IndexError("Row is out of bounds")
        elif column not in range(self.size_board):
            raise IndexError("Column is out of bounds")
        elif self.board[row][column] != '-':
            raise ValueError("Cell is taken")
       # if the whole board has been won, then no additional moves can be made
        elif self.square_won:
            raise ValueError("This board has already been won by player " + self.winner)
        
        # else we will update the board:
        else:
            self.board[row][column] = player_name
            # update column and row counts
            self.update_and_check_win("column" + str(column), player_name)
            self.update_and_check_win("row" + str(row), player_name)
            
            # if the row and the column are the same or add up to the length of the board - 1
            # then we know we have added to a diagnol
            if row == column:
                self.update_and_check_win("diagonal_top_left", player_name)
            
            if row + column == self.size_board - 1:
                self.update_and_check_win("diagonal_top_right", player_name)

            self.fill_count += 1
            
    """
    method to check if board is tied aka if it's all filled up
    but nobody has won
    :returns: boolean of whether it's a tie
    """
    def is_tie(self):
        if self.fill_count == self.size_board*self.size_board:
                if not self.square_won:
                    return True
        return False

    """
    updates our win_check dictionary
    :param key: key to the dictionary
    :param player_name: player to be updated for
    :returns: nothing, updates state
    """
    def update_and_check_win(self, key, player_name):
        self.win_check[(key, player_name)] += 1

        # if we've reached the total need to win this certain way
        if self.win_check[(key, player_name)] == self.size_board:
            self.square_won = True
            self.winner = player_name
    
