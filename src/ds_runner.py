from desmume.emulator import DeSmuME
import json

class DS_Runner:
    def __init__(self):
        with open("priv_config.json", "r") as fp:
            self.file_location = json.load(fp)["file_location"]

        self.game_instance = DeSmuME()
        return
    
    def open_ds(self):
        self.game_instance.open(self.file_location)

        window = self.game_instance.create_sdl_window()
        
        # Run the emulation as fast as possible until quit
        while not window.has_quit():
            window.process_input()   # Controls are the default DeSmuME controls, see below.
            self.game_instance.cycle()
            window.draw()
        return
    
if __name__ == "__main__":
    ds_runner = DS_Runner()
    ds_runner.open_ds()