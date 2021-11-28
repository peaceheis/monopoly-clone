import PySimpleGUI as sg

from utils import complement

class Tile: 
    def __init__(self, name, position, color="#FFFFFF", owner=None): 
        self.position  = position
        self.name = name
        self.color = color #this is here to keep my test code from breaking
        self.owner = owner #this is too.

    #land on the property
    def land(self, player, game, avoid_go_passing=False): 
        player.position = self.position
        if player.previous_position > player.position and avoid_go_passing==False: 
            player.balance += 200
            passed_go=True
        return passed_go #this project contains some of the hackiest code I've ever written, i'm sorry if you're reading trying to understand.

    def __repr__(self): 
        return f"Tile at position {self.position}, with name {self.name}"

    def get_frame(self): #that's funny because it returns a frame containing sg.T, and its a property? get it? 
        return sg.Frame("", layout=[
            [sg.T(self.name, text_color = complement(self.color), 
                  background_color=complement(self.color), justification="center")], 
            [sg.T("Owner:", background_color=self.color, justification="center")], 
            [sg.T(str(self.owner), background_color=self.color)]], background_color=self.color)

