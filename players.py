from enum import Enum

"""
This class is a simple enum to represent the players that can play
"""
class Player(Enum):
    O = 0
    X = 1

"""
ASCII representations of the players
"""
_ASCII_REPRESENTATIONS = {"O": " ___  \n/ _ \\ \n\___/ ", "X": "\ \/ /\n >  < \n/_/\_\\"}