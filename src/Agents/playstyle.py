from desmume.controls import Keys, keymask
from desmume.emulator import DeSmuME
from Misc.proper_controls import DSKeys

class PlayStyle:
    DEFAULT_START_INSTRUCTIONS = [
        DSKeys.KEY_START, # Start Menu
        DSKeys.KEY_A, # New Game
        DSKeys.KEY_A, # Selecting Boy
        DSKeys.KEY_A, # Selecting A
        DSKeys.KEY_START, # Hovering Confirm
        DSKeys.KEY_A, # Selecting Confirm
        DSKeys.KEY_LEFT, # Picking Yes
        DSKeys.KEY_A, # Selecting Yes
        DSKeys.KEY_A, # Selecting Balance Pack
        DSKeys.KEY_UP, # Hovering Yes
        DSKeys.KEY_A, # Picking Yes
        # Naming 1
        DSKeys.KEY_START,
        DSKeys.KEY_A,
        DSKeys.KEY_LEFT,
        DSKeys.KEY_A,
        # Naming 2
        DSKeys.KEY_START,
        DSKeys.KEY_A,
        DSKeys.KEY_LEFT,
        DSKeys.KEY_A,
        # Naming 3
        DSKeys.KEY_START,
        DSKeys.KEY_A,
        DSKeys.KEY_LEFT,
        DSKeys.KEY_A
    ]

    start_instructions : list[DSKeys]
    game_start_idx : int
    game_start_max_idx : int
    is_starting : bool

    def __init__(self, start_instructions : list[DSKeys] = DEFAULT_START_INSTRUCTIONS):
        self.start_instructions = start_instructions
        self.game_start_idx = 0
        self.game_start_max_idx = len(start_instructions)
        self.is_starting = True
        return
    
    def action_start(self) -> int:
        # Hard coded instructions to send to the game player
        return self._give_start_game_instructions()
    
    def _give_start_game_instructions(self) -> int:
        start_action = self.start_instructions[self.game_start_idx]
        print(f"TO DO START: {start_action.name} {start_action.value}")
        self.game_start_idx += 1
        if self.game_start_idx >= self.game_start_max_idx:
            self.is_starting = False
        return start_action.value
    
    # Functions to dictate specific play that may be inherited and/or
    # overidden
    
    def action_play(self) -> int:
        return None

    def select_action(self, do_start_actions : bool = True) -> int:
        # Only do start_actions first
        if do_start_actions and self.is_starting:
            return self.action_start()
        else:
            return self.action_play()
        
    def get_is_starting(self) -> bool:
        return self.is_starting