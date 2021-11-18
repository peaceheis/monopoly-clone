import json
from tile import Tile

class Property(Tile): 
    def __init__(self, name, price, house_price, hotel_price, group, is_owned=False, is_mortgaged=1, owner=None, rent = [], num_houses=0, is_mortgaged =False): 
        self.name = name
        self.price = price
        self.house_price = house_price
        self.hotel_price = hotel_price
        self.group = group
        group.add(self)
        self.is_owned = is_owned
        self.owner=owner
        self.rent: list = rent
        self.num_houses = num_houses 
        self.is_mortgaged = is_mortgaged
        #there's a lot to properties!
    
    def land(self, player): 
        if player.owns(self): 
            return f"{player.name} landed on {self.name}, which belongs to them."
        elif self.is_mortgaged: 
            return f"{player.name} landed on mortgaged property, {self.name}"
        else: 
            return player.deduct(self.rent[self.num_houses] * self.is_mortgaged)
        
    def develop(self, player): 
        player.charge(self.group.house_cost)
        self.num_houses += 1

    def mortgage(self, player): 
        self.is_mortgaged = 0
        player.add(self.price / 2)

    def unmortgage(self, player): 
        self.is_mortgaged = 1
        player.charge(self.price * 1.10)

    def buy(self, player): 
        player.deduct(self.price)
        self.owner = player
        self.is_owned = True
