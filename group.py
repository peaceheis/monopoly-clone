import json

class Group: 
    def __init__(self, name, color: str, house_cost: int): 
        self.color = color
        self.name = name
        self.house_cost = house_cost
        self.properties = []
        self.num_properties = 0
        
    def add(self, property): 
        self.properties.append(property)
        self.num_properties += 1
        

    
