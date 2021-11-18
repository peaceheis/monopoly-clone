import random

from tile import Tile

class CardTile(Tile): #acts like a deck of cards
    def __init__(self, cards): 
        self.cards = shuffle(cards)
        self.length = len(cards)
        self.card_index = 0

    def land(self):
        exec(self.cards[self.card_index])
        self.card_index = self.card_index + 1 % self.length

def shuffle(arr): 
    shuffled = []
    length = len(arr)

    for i in range(length): 
        shuffled.append(random.randrange(0, length))
    
    return shuffled


#grindy stuff