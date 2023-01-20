from unicodedata import numeric
import random

class AlwaysN():
    def __init__(self, n=2):
        self.type = "always_" + str(n)
        self.n = n
    
    def get_action(self):
        return(self.n)

    def give_result(self, opponent_action):
        pass


class RandomInRange():
    def __init__(self):
        self.type = "random"
        self.choices = range(0,5)

    def get_action(self):
        return(random.choice(self.choices))

    def give_result(self, opponent_action):
        pass
    

class Copycat():
    # Chooses 2 on first turn, then copies opponent's previous action in subsequent turns
    def __init__(self):
        self.type = "copycat"
        self.opp_prev_action = 2
        
    def get_action(self):
        return(self.opp_prev_action)
        
    def give_result(self, opponent_action):
        self.opp_prev_action = opponent_action


class TitForTat():
    def __init__(self):
        self.type = "titfortat"
        self.threshold = 2.5
        self.collaborate = 2
        self.retaliate = "copy"
        self.opp_prev_action = 2

    def get_action(self):
        if self.opp_prev_action > self.threshold:
            return self.opp_prev_action if self.retaliate == "copy" else self.retaliate
        else: 
            return random.choice(range(2,4)) if self.collaborate == "2or3" else self.collaborate

    def give_result(self, opponent_action):
        self.opp_prev_action = opponent_action

class Forgiver():
    def __init__(self):
        self.type = "forgiver"
        self.threshold = 2.5
        self.collaborate = 2
        self.retaliate = "copy"
        self.prev_action = 0
        self.opp_prev_action = 2
        self.forgive_after = 3
        self.history = []

    def get_action(self):
        if sum([h > 5 for h in self.history]) >= self.forgive_after:
            self.prev_action = 2
        else:
            if self.opp_prev_action > self.threshold:
                self.prev_action = self.opp_prev_action if self.retaliate == "copy" else self.retaliate
            else: 
                self.prev_action = random.choice(range(2,4)) if self.collaborate == "2or3" else self.collaborate
        return self.prev_action

    def give_result(self, opponent_action):
        self.history.append(self.prev_action + opponent_action)
        if len(self.history) > self.forgive_after:
            self.history.pop(0)