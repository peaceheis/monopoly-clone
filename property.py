import json

import group

class Property: 
    def __init__(self, name, price, house_price, hotel_price, group: group.Group): 
        self.name = name
        self.price = price
        self.house_price = house_price
        self.hotel_price = hotel_price
        group.add(self)

