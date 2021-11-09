class Player:
    def __init__(self, name):
        self.name = name
        self.balance = 1500

    def evaluate_state(self): 
        if self.balance == 0: 
            return True