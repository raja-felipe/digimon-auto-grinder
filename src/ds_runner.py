from desmume.emulator import DeSmuME, SCREEN_HEIGHT, SCREEN_HEIGHT_BOTH, SCREEN_WIDTH
import json
import multiprocessing
from playstyle import PlayStyle
from randomPlayStyle import RandomPlayStyle
from desmume.controls import keymask, Keys
import time
from PIL import Image
import inspect

class DS_Runner:
    def __init__(self, playstyle: PlayStyle, dl_name=None):
        with open("priv_config.json", "r") as fp:
            self.file_location = json.load(fp)["file_location"]

        self.game_instance = DeSmuME(dl_name)
        self.play_mode = playstyle
        self.prev_action = 1
        self.window = None
        return
    
    def buffer_to_image(self, buffer):
        """
        Convert the display buffer (memoryview) to an image.
        """
        # Create an image from the buffer
        image = Image.frombuffer('RGBA', (SCREEN_WIDTH, SCREEN_HEIGHT_BOTH), buffer, 'raw', 'RGBX', 0, 1)
        return image
    
    def open_ds(self):
        self.game_instance.open(self.file_location)
        return
    
    def play_ds(self):
        # for _ in range(180):
        #     curr_action = self.get_action()
        #     self.press_key(curr_action)
        #     self.unpress_key()
        # self.buffer_to_image(self.game_instance.display_buffer_as_rgbx()).show()

        window = self.game_instance.create_sdl_window()
        prev_input = Keys.KEY_NONE
        self.unpress_all_keys()
        # self.game_instance._savestate.load(1)

        # These are needed as you need to assign each frame individually
        # to press and unpress buttons
        FRAME_COUNT_TO_PRESS = 120
        curr_frame_count = 0

        # Run the emulation as fast as possible until quit
        while not window.has_quit():

            window.process_input()

            if curr_frame_count == FRAME_COUNT_TO_PRESS:
                curr_action = self.play_mode.play()
                print("PRESSED ACTION:", curr_action)
                self.game_instance.input.keypad_add_key(curr_action)
                prev_input = curr_action
                curr_frame_count = 0
            else:
                if curr_frame_count == 0:
                    print("UNPRESSING ACTION:", prev_input)
                    self.game_instance.input.keypad_rm_key(prev_input)
                curr_frame_count += 1
            # print(f"CURR ACTION: {self.game_instance.input.keypad_get()}")  

            self.game_instance.cycle(with_joystick=False)
            window.draw()


    def press_key(self, key : int, time_pressed : float = 3):
        """
        use this to press the button designated for the key
        """
        print(f"Going to press: {key}")
        self.game_instance.input.keypad_add_key(key)
        print("Current Keypad: ", self.game_instance.input.keypad_get())
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
        print(f"Going to release: {self.prev_action}")
        self.game_instance.input.keypad_rm_key(self.prev_action)
        print("Current Keypad: ", self.game_instance.input.keypad_get())
        return
    
    def unpress_all_keys(self):
        # print(inspect.getmembers(Keys()))
        for key in inspect.getmembers(Keys()):
            key_name = key[0]
            key_val = key[1]
            if not key_name.startswith("_") and key_name != "NB_KEYS" and key_name != "NO_KEY_SET":
                self.game_instance.input.keypad_rm_key(key_val)
    
    def get_action(self) -> int:
        return self.play_mode.play()
    
    # def act(self):
    #     self.press_key(self.play_mode.play())
    
if __name__ == "__main__":
    random_playstyle = PlayStyle()
    ds_runner = DS_Runner(playstyle=random_playstyle)
    ds_runner.open_ds()
    # print(ds_runner.game_instance.is_running())
    ds_runner.play_ds()