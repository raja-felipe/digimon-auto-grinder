from desmume.emulator import DeSmuME
import json
import multiprocessing
from playstyle import PlayStyle
from randomPlayStyle import RandomPlayStyle
from desmume.controls import keymask
import time

class DS_Runner:
    def __init__(self, playstyle: PlayStyle, dl_name=None):
        with open("priv_config.json", "r") as fp:
            self.file_location = json.load(fp)["file_location"]

        self.game_instance = DeSmuME(dl_name)
        self.play_mode = playstyle
        self.prev_action = 1
        return
    
    def open_ds(self):
        self.game_instance.open(self.file_location)
        return
    
    def play_ds(self):
        window = self.game_instance.create_sdl_window()
        
        # Run the emulation as fast as possible until quit
        while not window.has_quit():
            window.process_input()   # Controls are the default DeSmuME controls, see below.
            curr_action = self.get_action()
            self.press_key(curr_action)
            self.game_instance.cycle(with_joystick=False)
            self.unpress_key()
            window.draw()


    def press_key(self, key : int, time_pressed : float = 3):
        """
        use this to press the button designated for the key
        """
        print(f"Going to press: {key}")
        self.game_instance.input.keypad_add_key(keymask(key))
        print(self.game_instance.input.keypad_get())
        self.prev_action = key
        # curr_time = time.time()
        # while (time.time() - curr_time < time_pressed):
        #     continue
        # print(f"Going to release: {key}")
        return
    
    def unpress_key(self, time_pressed : float = 3):
        """
        use this to press the button designated for the key
        """
        print(f"Going to press: {self.prev_action}")
        self.game_instance.input.keypad_rm_key(keymask(self.prev_action))
        return
    
    def get_action(self) -> int:
        return self.play_mode.play()
    
    # def act(self):
    #     self.press_key(self.play_mode.play())
    
if __name__ == "__main__":
    random_playstyle = PlayStyle()
    ds_runner = DS_Runner(playstyle=random_playstyle)
    ds_runner.open_ds()
    ds_runner.play_ds()
    # ds_runner_2 = DS_Runner()
    # ds_runner_2.open_ds()