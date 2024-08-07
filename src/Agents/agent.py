"""

Super class for Agents that will be playing Digimon

"""

from Agents.playstyle import PlayStyle
from Agents.randomPlayStyle import RandomPlayStyle
from Misc.proper_controls import DSKeys

class Agent():

    DEFAULT_START_INSTRUCTIONS = [
        DSKeys.KEY_START,
        DSKeys.KEY_A,
        DSKeys.KEY_A,
        DSKeys.KEY_START,
        DSKeys.KEY_A
    ]

    play_style : PlayStyle
    start_instructions : list[int]
    
    def __init__(self, play_style : PlayStyle, 
                 start_instructions : list[int] = DEFAULT_START_INSTRUCTIONS):
        self.play_style = play_style
        self.start_instructions = start_instructions
        return
    
    def start_game(self):
        # Hard coded instructions to send to the game player
        return
    
    def _give_start_game_instructions(self):
        
        return