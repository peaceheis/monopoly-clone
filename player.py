class Player:
    def __init__(self, name, properties=[], complete_groups = [], num_railroads = 0, num_utilities=0, position=0):
        self.name = name
        self.balance = 1500
        self.properties = properties
        self.complete_groups = complete_groups
        self.num_railroads = num_railroads
        self.num_utilies = num_utilities
        self.position = position

    def evaluate_state(self): 
        if self.balance == 0: 
            return True

    def owns(self, property):
        return property in self.properties

    def give(self, amount): 
        self.balance += amount

    def charge(self, amount): 
        self.balance -= amount
        return True if not self.is_bankrupt() else False

    def is_bankrupt(self): 
        return self.balance < 0

    def buy(self, property): 
        if self.balance < property.price(): 
            return False
        self.properties.append(property)
        
        #check if a group has been made. 
        group = property.group

        has_made_group = True

        for property in group.properties: 
            if not self.owns(property): 
                property

        return has_made_group
            