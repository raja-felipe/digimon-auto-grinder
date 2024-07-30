from desmume.controls import Keys, keymask
from desmume.emulator import DeSmuME

class PlayStyle:
    def __init__(self):
        return
    
    def play(self) -> int:
        """
        play returns the action the emulator should do
        """
        print(Keys.KEY_A)
        return Keys.KEY_A
