class Player:
    """A code representation of a player."""
    def __init__(self, name, balance = 1500, properties=[], complete_groups = [], num_railroads = 0, num_utilities=0, previous_position = None, position=0):
        self.name = name
        self.balance = balance
        self.properties = properties
        self.complete_groups = complete_groups
        self.num_railroads = num_railroads
        self.num_utilies = num_utilities
        self.previous_position = previous_position
        self.position = position

    def evaluate_state(self): 
        if self.balance == 0: 
            return True

    def owns(self, property):
        return property in self.properties

    def charge(self, amount): 
        self.balance -= amount
        return True if not self.is_bankrupt() else False

    def is_bankrupt(self): 
        return self.balance < 0

    def buy(self, property): 
        if self.balance < property.price(): 
            return False, False
        self.properties.append(property)
        
        #check if a group has been made. 
        group = property.group

        has_made_group = True

        for property in group["properties"]: 
            if not self.owns(property): 
                has_made_group = False

        return True, has_made_group

    def __str__(self): 
        return self.name
            