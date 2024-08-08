from Agents.playstyle import PlayStyle
from Misc.proper_controls import DSKeys
import random

class RandomPlayStyle(PlayStyle):
    def __init__(self):
        super().__init__()
        self.key_values = [key.value for key in DSKeys]
        return
    
    def action_play(self):
        random_move = random.choice(self.key_values)
        print(random_move)
        return random_move

