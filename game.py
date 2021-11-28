from inspect import isgeneratorfunction
import json
from os import name
import random
import sys

import PySimpleGUI as sg

from utils import *
from property import *
from specials import *
from player import Player
from tile import Tile
from cards import CardTile


class Game:
    """In charge of both rendering and stitching everything together."""
    def __init__(self, players=[], turn=0, dice=[1, 1]):
        self.groups = self.load_groups()
        self.streets, self.railroads, self.utilities, self.comm_chests, self.chances, self.corners, self.tax = self.load_tiles()
        self.tiles = self.streets + self.railroads + self.utilities + self.comm_chests + self.chances + self.corners + self.tax
        self.tiles.sort(key=lambda prop: prop.position)
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
        self.tiles[player.position].land(player, self)
        self.players[self.turn] = player

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

        # load streets
        streets: dict = props["streets"]

        initialized_streets = []
        for key in streets.keys():
            val = streets[key]
            grp: dict = self.groups[val["group"]]
            prop = StreetTile(val["name"], int(key), val["cost"], grp["house cost"], grp)
            self.groups[val["group"]]["properties"].append(prop)
            initialized_streets.append(prop)

        # load railroads
        rails: dict = props["railroads"]
        config: dict = props["railroad config"]

        initialized_rails = []
        for key in rails.keys():
            val = rails[key]
            prop = Railroad(val + " Railroad", int(key), config["cost"], config["rent"])
            initialized_rails.append(prop)

        # load utilities
        utils: dict = props["utilities"]
        config: dict = props["utility config"]

        initialized_utils = []
        for key in utils.keys():
            val = utils[key]["name"]
            prop = Utility(val, int(key), config["cost"], config["rent"])
            initialized_utils.append(prop)

        # load action properties
        chance, comm_chest = json.load(open("tiles.json"))["actions"]["chance"], \
                             json.load(open("tiles.json"))["actions"]["community chest"]
        # TODO, handle chance, comm_chest

        initialized_chance = [Tile("chance", int(key)) for key in chance.keys()]
        initialized_comm_chest = [Tile("community chest", loc) for loc in comm_chest["locs"]]

        # TODO, do corner things
        corners = json.load(open("tiles.json"))["corners"]
        initialized_corners = [Tile(corners[key], int(key)) for key in corners.keys()]

        #TODO, do tax things
        tax = json.load(open("tiles.json"))["tax"]
        initialized_tax = [TaxTile(int(key), tax[key][0], tax[key][1]) for key in tax.keys()]

        return initialized_streets, initialized_rails, initialized_utils, initialized_comm_chest, initialized_chance, initialized_corners, initialized_tax

    # PRE-GAME SELECTIONS

    def intro(self):
        sg.change_look_and_feel("LightBrown13")
        # options for loading game from save or creating a new game

        layout = [[sg.T("Welcome to The Game Of", justification="left", expand_x=True, expand_y=True, font="bold")],
                  get_logo(50, "center"),
                  [sg.B("Load Game From Save", size=(20, 1.5), expand_x=True),
                   sg.B("New Game", size=(20, 1.5), expand_x=True)]]
        window = sg.Window("MONOPOLY", layout=layout).finalize()
        event, values = window.read()

        match event:
            case "Load Game From Save":
                # display window for loading save
                window.close()
                layout = [[sg.T("Click to Browse Files", pad=(10, 10)),
                           sg.FileBrowse("Browse File", file_types="*.json", pad=(10, 10)), sg.Ok("Load")]]
                window = sg.Window("Load Save File", layout=layout)
                event, values = window.read()

            case "New Game":
                window.close()
                game = Game()

                # ask number of players
                layout = [[sg.T("How many players?")],
                          [sg.Spin([2, 3, 4, 5, 6, 7, 8], initial_value=2, key="-SPIN-"), sg.Ok()]]
                window = sg.Window("Number of Players", layout=layout)
                event, values = window.read()
                window.close()

                if event == sg.WINDOW_CLOSED:
                    sys.exit()

                self.num_players = values["-SPIN-"]

                # player names
                column = [[sg.T(f"Player {i + 1}"), sg.Input("Input", key=f"-Player {i}-")] for i in
                          range(self.num_players)]
                layout = [[sg.T("What are each of the players' names?")],
                          column,
                          [*get_logo(15, "right"), sg.Ok("Let's Go!", button_color="teal")]]

                window = sg.Window("Name Selection", layout=layout)
                event, values = window.read()
                window.close()

                if event == sg.WINDOW_CLOSED:
                    sys.exit()

                self.players = [Player(name) for name in values.values()]
                # self.num_players

            case sg.WINDOW_CLOSED:
                window.close()

    def draw_window(self):
        """
        column_1_layout = [sg.T(tile.name) for tile in self.tiles[0:12]]
        alt_layout = [get_logo(20, "left"), 
                      []]"""

        frame_layout = [[sg.B("Roll Dice"), sg.B("Trade"), sg.B("End Turn")], 
                        [sg.B("Mortgage/Unmortgage"), sg.B("Build/Sell Houses and Hotels"), sg.B("Save & Quit")]]

        frame = sg.Frame("Actions", layout=frame_layout, expand_x=True, expand_y=True)
        layout = [get_logo(20, "left"),
                 [tile.get_frame() for tile in self.tiles[20:31]],
                  [frame]]
        event, values = sg.Window("Monopoly", layout=layout).read()



game = Game()
game.intro()
game.draw_window()