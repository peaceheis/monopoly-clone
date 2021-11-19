import json
import random

import PySimpleGUI as sg
from property import Property
from specials import Railroad, Utility
from player import Player


class Game: 
    def __init__(self, players=[], turn=0, dice=[1, 1]):
        if (self.get_save_if_possible()) is not None: 
            self.should_load_save = True #i suspect this is unpythonic.        

        self.groups = self.load_groups()
        self.players = players
        self.num_players = len(players)
        self.turn = turn
        self.dice = dice

    def get_save_if_possible(self): 
        pass

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

    def load_groups(self): 
        return json.load(open("groups.json"))["groups"]

    def load_tiles(self):
        props = json.load(open("tiles.json"))["properties"]
        
        #load streets
        streets: dict = props["streets"]
       
        initialized_streets = []
        for key in streets.keys():
            val = streets[key]
            grp: dict = self.groups[val["group"]]
            prop = Property(val["name"], int(key), val["cost"], grp["house cost"], grp)
            self.groups[val["group"]]["properties"].append(prop)
            initialized_streets.append(prop)

        #load railroads
        rails: dict = props["railroads"]
        config: dict = props["railroad config"]

        initialized_rails = []
        for key in rails.keys(): 
            val = rails[key]
            prop = Railroad(val, int(key), config["cost"], config["rent"])
            initialized_rails.append(prop)

        #load utilities
        utils: dict = props["utilities"]
        config: dict = props["utility config"]

        initialized_utils = []
        for key in utils.keys(): 
            val = utils[key]
            prop = Utility(val, int(key), config["cost"], config["rent"])
            initialized_utils.append(prop)

        return initialized_streets, initialized_rails, initialized_utils

            


g = Game()
g.load_tiles()