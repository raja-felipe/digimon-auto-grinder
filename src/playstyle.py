from desmume.controls import Keys, keymask
from desmume.emulator import DeSmuME

class PlayStyle:
    def __init__(self):
        self.prev_played = Keys.KEY_B
        self.loop_button = Keys.KEY_B
        self.control_sequence = [keymask(Keys.KEY_START), Keys.KEY_B]

        self.input_index = 0
        return
    
    def play(self) -> int:
        """
        play returns the action the emulator should do
        """
        if self.input_index == len(self.control_sequence):
            self.input_index = 0

        
        play_key = self.control_sequence[self.input_index]
        self.input_index += 1
        
        # print(play_key)
        return play_key
