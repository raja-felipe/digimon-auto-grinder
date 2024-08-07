from Agents.playstyle import PlayStyle
from Misc.proper_controls import DSKeys

class TestPlaystyle(PlayStyle):

    def __init__(self):
        self.prev_played = DSKeys.KEY_B
        self.loop_button = DSKeys.KEY_B
        self.control_sequence = [DSKeys.KEY_START, DSKeys.KEY_B]

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