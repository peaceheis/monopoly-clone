import json
import math

import PySimpleGUI as sg

from tile import Tile
from utils import complement, get_logo

class OwnedTile(Tile): 
    def __init__(self, name, position, price, rent, is_owned=False, is_mortgaged=1, owner=None,rent_index=0, color="#FFFFFF"):
        super().__init__(name, position, color=color)
        self.price = price
        self.is_owned = is_owned
        self.owner = owner
        self.rent = rent
        self.rent_index = rent_index
        # ^this points to what index in the rent array will be used. for Street properties, this is the number of houses/hotels,
        # with railroads/utilities, this is the number of the type of property owned. 
        self.is_mortgaged = is_mortgaged #1 or 0, this just gets multiplied after all other rent calculations.

    def land(self, player, game, avoid_go_passing=False): 
        super().land(player, game, avoid_go_passing=avoid_go_passing)
        if self.is_owned: 
            if self.owner != player: 
                player.charge(self.rent[self.rent_index]) #TODO, update games window with appropriate information
            else: 
                pass
                #update window accordingly
        else: 
            event, values = sg.Window(f"Buy Options for {self.__class__.__name__} {self.name}", layout = 
            [[sg.T(f"Would you like to buy {self.name} for ${self.price}, or auction it?")], 
              [sg.B("Buy"), sg.B("Auction")],
              get_logo(10, "right")], grab_anywhere=True, color=self.color, no_titlebar=True).read()
            
            match event: 
                case "Buy": 
                    if player.balance < self.price: 
                        sg.Popup("Not enough money, auctioning instead", title="Insufficient Funds")
                        game.auction(math.floor(self.price*.75)) 
                        return #do something better
                    player.charge(self.rent[self.rent_index])

                case "Auction": 
                    game.auction(math.floor(self.price*.75))

    def get_frame(self): 
        layout = [[]]

class StreetTile(OwnedTile):
    def __init__(self, name, position, price, rent, house_price, group, is_owned=False, is_mortgaged=1, owner=None, num_houses=0):
        super().__init__(name, position, price, rent, is_owned=is_owned, is_mortgaged=is_mortgaged, owner=owner, rent_index=num_houses)
        self.house_price = house_price
        self.group = group
        self.color = self.group["color"]
        self.num_houses = num_houses
        group["properties"].append(self)

    def land(self, player, game, avoid_go_passing=False):
        passed_go = super().land(player, game, avoid_go_passing=avoid_go_passing)
        if player.owns(self):
            return passed_go, f"{player.name} landed on {self.name}, which belongs to them."
        elif self.is_mortgaged:
            return passed_go, f"{player.name} landed on mortgaged property, {self.name}"
        else:
            return passed_go, player.deduct(self.rent[self.num_houses] * self.is_mortgaged) #FIXME this is all horrible 

    def develop(self, player):
        player.charge(self.group.house_cost)
        self.num_houses += 1
        self.rent_index += 1

    def mortgage(self, player):
        self.is_mortgaged = 0
        player.balance += self.price / 2

    def unmortgage(self, player):
        self.is_mortgaged = 1
        player.charge(self.price * 1.10)

    def buy(self, player):
        player.deduct(self.price)
        self.owner = player
        self.is_owned = True

    def __repr__(self):
        return f"{self.position }: Property {self.name} costing {self.price}, and part of group {self.group['name']}\n"

class Railroad(OwnedTile): 
    def __init__(self, name, position, price, is_owned=False, is_mortgaged=1, owner=None, rent=[], rent_index=0, color="#000000"): 
        super().__init__(name, position, price, is_owned=is_owned, is_mortgaged=is_mortgaged, owner=owner, rent=rent, 
                         rent_index=rent_index, color=color)

    def land(self, player, game): 
        return player.charge(self.rent * player.num_railroads)

    def __repr__(self): 
        return f"Property {self.name}, at position {self.position}, costing {self.price}."

class Utility(OwnedTile): 
    def __init__(self, name, position, price, rent, is_owned=False, is_mortgaged=1, owner=None): 
        super().__init__(position, name=name)
        self.price = price
        self.rent = rent
        self.is_owned = is_owned
        self.is_mortgaged = is_mortgaged
        self.owner = owner

    def land(self, player, game): 
        return player.charge(self.rent[player.num_railroads] * (game.dice[0] + game.dice[1]))
    
    def __repr__(self): 
        return f"Property {self.name}, at position {self.position}, costing {self.price}." 