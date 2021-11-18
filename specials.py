from property import Property

class Railroad(Property): 
    def land(self, player): 
        return player.charge(self.rent * player.num_railroads)

class Utility(Property): 
    def land(self, player): 
        return player.charges(self.rent[player.num_railroads] * )