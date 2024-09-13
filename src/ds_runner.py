from desmume.emulator import DeSmuME, DeSmuME_SDL_Window, SCREEN_HEIGHT, SCREEN_HEIGHT_BOTH, SCREEN_WIDTH
import json
import multiprocessing
from Agents.agent import Agent
from Agents.playstyle import PlayStyle
from Agents.test_playstyle import TestPlayStyle
from Agents.randomPlayStyle import RandomPlayStyle
from desmume.controls import keymask, Keys
import time
from PIL import Image
import inspect

TICK_RATE = 120
FRAME_COUNT_TO_PRESS = 1
FRAME_COUNT_TO_START = 180
FRAMES_TO_WAIT = 660

class DS_Runner:

    file_location : str
    curr_frame_count : int
    curr_frames_to_wait: int
    game_instance : DeSmuME
    play_style : PlayStyle
    prev_action : int
    window : DeSmuME_SDL_Window

    def __init__(self, playstyle: PlayStyle, dl_name=None):
        with open("priv_config.json", "r") as fp:
            self.file_location = json.load(fp)["file_location"]
        self.curr_frame_count = 0
        self.game_instance = DeSmuME(dl_name)
        self.play_style = playstyle
        self.prev_action = Keys.KEY_NONE
        self.window = None
        self.curr_frames_to_wait = FRAMES_TO_WAIT
        return
    
    def buffer_to_image(self, buffer):
        """
        Convert the display buffer (memoryview) to an image.
        """
        # Create an image from the buffer
        image = Image.frombuffer('RGBA', (SCREEN_WIDTH, SCREEN_HEIGHT_BOTH), buffer, 'raw', 'RGBX', 0, 1)
        return image
    
    def tick(self, tick_count:int) -> None:
        for _ in range(tick_count):
            self.game_instance.cycle(False)
    
    def open_ds(self):
        self.game_instance.open(self.file_location)
        return
    
    def wait_for_title_screen(self):
        # print(f"frames left : {self.curr_frames_to_wait}")
        self.curr_frames_to_wait -= 1
        return
    
    def play_ds(self):
        window = self.game_instance.create_sdl_window()
        self.unpress_all_keys()

        # Run the emulation as fast as possible until quit
        while not window.has_quit():
            window.process_input()

            if self.curr_frames_to_wait > 0:
                self.wait_for_title_screen()

            elif self.play_style.get_is_starting():
                self.do_button_press(FRAME_COUNT_TO_START)
            
            else:
                self.do_button_press(FRAME_COUNT_TO_PRESS)  

            self.game_instance.cycle(with_joystick=False)
            # self.tick(TICK_RATE)
            window.draw()

    def do_button_press(self, frame_timer:int):
        if self.curr_frame_count == frame_timer:
            self.press_action_key()
        else:
            if self.curr_frame_count == 0:
                self.unpress_action_key()
            self.curr_frame_count += 1
        # print(f"CURR ACTION: {self.game_instance.input.keypad_get()}")  
    def press_action_key(self, time_pressed : float = 3):
        """
        use this to press the button designated for the key
        """
        curr_action = self.get_action()
        print("PRESSED ACTION:", curr_action)
        self.game_instance.input.keypad_add_key(curr_action)
        self.prev_action = curr_action
        self.curr_frame_count = 0
        # curr_time = time.time()
        # while (time.time() - curr_time < time_pressed):
        #     continue
        # print(f"Going to release: {key}")
        return
    
    def unpress_action_key(self, time_pressed : float = 3):
        """
        use this to press the button designated for the key
        """
        # print("UNPRESSING ACTION:", self.prev_action)
        self.game_instance.input.keypad_rm_key(self.prev_action)
        # print("Current Keypad: ", self.game_instance.input.keypad_get())
        return
    
    def unpress_all_keys(self):
        for key in inspect.getmembers(Keys()):
            key_name = key[0]
            key_val = key[1]
            if not key_name.startswith("_") and key_name != "NB_KEYS" and key_name != "NO_KEY_SET":
                self.game_instance.input.keypad_rm_key(key_val)
    
    def get_action(self) -> int:
        return self.play_style.select_action()
    
if __name__ == "__main__":
    selected_playstyle = RandomPlayStyle()
    ds_runner = DS_Runner(playstyle=selected_playstyle)
    ds_runner.open_ds()
    ds_runner.play_ds()