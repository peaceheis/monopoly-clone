import json 

from constants import *
import group
from card import Card
from player import Player


class Game: 
    def __init__(self):
        self.groups = group.initialize_groups()
        self.players = []
        
        self.get_players()

    def load_tiles(self):
        pass

    def load_cards(self): 
        pass

    def get_players(self): 
       pass
    
    def should_continue_game(self): 
        pass

    def game(self):
        pass

    def save_game(self): 
        pass

    def load_save(self): 
        pass



Game()