import json
import random

from constants import *
import group
from player import Player


class Game: 
    def __init__(self, players=[], turn=0, dice=[1, 1]):
        self.groups = self.load_groups()
        self.players = players
        self.num_players = len(players)
        self.turn = turn
        self.dice = dice
        
        self.get_players()

    def load_tiles(self):
        streets = json.load(open("tiles.json"))["properties"]["streets"]

    def turn(self): 
        self.turn = self.turn + 1 % self.num_players
        player = self.players[self.turn]
        self.popup(f"{player}'s turn!")
        self.roll_dice_visually()
        self.dice = [random.randrange(1, 7) for i in range(2)]
        player.position = player.position + self.dice % 36


    def popup(self, msg): 
        pass
    
    def post(self, msg): 
        pass

    def roll_dice_visually(self): 
        pass    
    
    def auction(self):
        pass
    
    def should_continue_game(self): 
        pass


    def save_game(self): 
        pass

    def load_save(self): 
        pass

    def load_groups() -> list: 
        groups: dict = json.load(open("groups.json"))["groups"]

        initalized_groups = []
        for val in groups.values() : 
            prop = group.Group(val["name"], val["color"], val["house cost"])
            initalized_groups.append(prop)

        return initalized_groups 


winCount, loseCount = 0

Game()