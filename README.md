# Super Tic Tac Toe

This project is written in python3. To run it simply clone the repo and from the folder run `python3 game.py`

The code is written in three main components as follows:

# Single Board

A python class to define a single tic tac toe game. The game is represented by an array, which is updated by the `play_square` method. It keeps track of the winner of the board as well as if the board is a tie or not. It uses a dictionary to keep track of all the ways the board can be won by a player and updates the dictionary accordingly after each moves. While this may seem more complicated than iterating over the board to determine if a player has won, it allows for a check in constant time and I feel that the code itself is simpler.


# Meta Board

A python class to keep track of the super tic tac toe game. There is a 2d array of SingleBoards to keep track of the game.  It uses the single board functions to update after a move on the overall board. 

# Game

Keeps track of the game logic, like who's turn it is, if each player is a computer or human, and input processing. If there is a computer playing, there is a list of possible moves remaining that is updated to keep track for the computer to choose at random. 
