from property import Property

class Railroad(Property): 
    def __init__(self, name, position, price, rent, is_owned=False, is_mortgaged=1, owner=None): 
        self.name = name
        self.position = position
        self.price = price
        self.rent = rent
        self.is_owned = is_owned
        self.is_mortgaged = is_mortgaged
        self.owner = owner

    def land(self, player, game): 
        return player.charge(self.rent * player.num_railroads)

class Utility(Property): 
    def __init__(self, name, position, price, rent, is_owned=False, is_mortgaged=1, owner=None): 
        self.name = name
        self.position = position
        self.price = price
        self.rent = rent
        self.is_owned = is_owned
        self.is_mortgaged = is_mortgaged
        self.owner = owner


    def land(self, player, game): 
        return player.charge(self.rent[player.num_railroads] * (game.dice[0] + game.dice[1]))