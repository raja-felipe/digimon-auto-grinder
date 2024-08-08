from Agents.playstyle import PlayStyle
from Misc.proper_controls import DSKeys

class TestPlayStyle(PlayStyle):

    def __init__(self):
        super().__init__()
        self.prev_played = DSKeys.KEY_B.value
        self.loop_button = DSKeys.KEY_B.value
        self.control_sequence = [DSKeys.KEY_START.value, DSKeys.KEY_B.value]

        self.input_index = 0

        return
    
    def action_play(self) -> int:
        """
        play returns the action the emulator should do
        """
        if self.input_index == len(self.control_sequence):
            self.input_index = 0

        
        play_key = self.control_sequence[self.input_index]
        self.input_index += 1
        
        # print(play_key)

        return play_key