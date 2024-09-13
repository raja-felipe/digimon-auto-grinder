"""

Super class for Agents that will be playing Digimon

"""

from Agents.playstyle import PlayStyle
from Agents.randomPlayStyle import RandomPlayStyle
from Misc.proper_controls import DSKeys

class Agent():

    play_style : PlayStyle
    
    def __init__(self, play_style : PlayStyle):
        self.play_style = play_style
        return