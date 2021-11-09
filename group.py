import json


class Group: 
    def __init__(self, name, color: str): 
        self.color = color
        self.name = name
        self.properties = []
        self.num_properties = 0
        
    def add(self, property): 
        self.properties.append(property)
        self.num_properties += 1
        
def initalize_groups(): 
    groups = json.load(open("groups.json"))["groups"]
    print(groups)
    initalized_groups = []
    for group in groups: 
        print(group)
        initalized_groups.append(Group(group["name"], group["color"]))

    return initalized_groups 
    
print(initalize_groups())