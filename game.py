from board import Board
from constants import *
from card import Card
from player import Player

class Game: 
    def __init__(self): 
        self.load_groups
        self.load_tiles
        self.load_board()
        self.get_players()

    def load_groups(self):
        pass

    def load_tiles(self):
        pass

    def load_board(self): 
        self.board = Board()
        self.board.root.geometry(f"{self.board.SCREEN_WIDTH}x{self.board.SCREEN_HEIGHT}")

        while self.should_continue_game(): 
            self.board.root.update_idletasks()
            self.board.root.update()



    def load_cards(self): 
        pass

    def get_players(self): 
       pass
    
    def should_continue_game(self): 
        return True

    def game(self):
        pass




Game()