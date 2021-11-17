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
        
def initalize_groups() -> list: 
    groups: dict = json.load(open("groups.json"))["groups"]

    initalized_groups = []
    for val in groups.values() : 
        prop = Group(val["name"], val["color"], val["house cost"])
        initalized_groups.append(prop)

    return initalized_groups 
    
