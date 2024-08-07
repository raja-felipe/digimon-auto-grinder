from desmume.controls import Keys, keymask
from desmume.emulator import DeSmuME
from Misc.proper_controls import DSKeys

class PlayStyle:
    DEFAULT_START_INSTRUCTIONS = [
        DSKeys.KEY_START,
        DSKeys.KEY_A,
        DSKeys.KEY_A,
        DSKeys.KEY_START,
        DSKeys.KEY_A
    ]

    start_instructions : list[int]

    def __init__(self, start_instructions : list[int] = DEFAULT_START_INSTRUCTIONS):
        self.start_instructions = start_instructions
        return
    
    def start_game(self):
        # Hard coded instructions to send to the game player
        return
    
    def _give_start_game_instructions(self):
        
        return
    
    def play(self) -> int:
        return None
