import random

import PySimpleGUI as sg

from tile import Tile

class CardTile(Tile): 
    def __init__(self, position, func_array=[]): 
        super().__init__(position)
        self.func_array = func_array
        self.num_options = self.func_array.length
        self.index = 0

    def land(self, player, game): 
        self.func_array[self.index](player, game)

class TaxTile(Tile): 
    def __init__(self, position, name, cost): 
        super().__init__(position, name=name)
        self.cost = cost

    def land(self, player, game): 
        return player.charge(self.cost)


class ChanceTile(CardTile):
    def __init__(self, position): 
        #i'm not encoding any more json, dang it! if you want to modify it you can edit the python, it's just as easy. (for me)

        def position_mover(position, msg): 
            def func(player, game, position, msg): 
                sg.Popup(msg, title="Chance action")
                player.position = position
                game.tiles[position].land(player, game) #my structuring of things is a little weird, i'm finding lol
            return func
        
    
        func_array = [position_mover(0, "Advance To Go. "), position_mover(24, "Advance to Illinois Avenue.")]

class CommChestTile(CardTile): 
    pass
