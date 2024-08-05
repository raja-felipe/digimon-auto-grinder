from desmume.controls import Keys, keymask
from desmume.emulator import DeSmuME

class PlayStyle:
    def __init__(self):
        self.prev_played = Keys.KEY_B
        self.loop_button = Keys.KEY_B

        self.input_index = 0
        self.max_inputs = 4
        return
    
    def play(self) -> int:
        """
        play returns the action the emulator should do
        """
        if self.input_index == self.max_inputs:
            self.input_index = 0

        controls_sequence = [Keys.KEY_A, Keys.KEY_UP, Keys.KEY_DOWN, Keys.KEY_B]
        play_key = controls_sequence[self.input_index]
        self.input_index += 1
        
        # print(play_key)
        return play_key
