class Player:
    def __init__(self, name, properties=[], complete_groups = []):
        self.name = name
        self.balance = 1500
        self.properties = properties
        self.complete_groups = complete_groups

    def evaluate_state(self): 
        if self.balance == 0: 
            return True

    def owns(self, property):
        return property in self.properties

    def deduct(self, amount): 
        self.balance -= amount