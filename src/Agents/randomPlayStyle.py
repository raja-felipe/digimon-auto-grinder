from playstyle import PlayStyle
from desmume.controls import Keys
import random

class RandomPlayStyle(PlayStyle):
    def __init__(self):
        super().__init__()
        self.key_values = [value for _, value in Keys.__dict__.items() if isinstance(value, int)]
        return
    
    def play(self):
        random_move = random.choice(self.key_values)
        print(random_move)
        return random_move

