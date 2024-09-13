"""
Script specifc to initializing the needed files for the autoplayer, including:
- game_file folder to store the .nds file containing a copy of Digimon World Dawn
- priv_config json file containing a line of the file location of game copy relative to repository
"""

import os
import json

def init_game_file_folder() -> None:
    print(os.path.exists("game_file"))
    if not os.path.exists("game_file"):
        os.makedirs("game_file")

def init_priv_config(game_file_location:str) -> None:
    priv_config_fname = "priv_config.json"
    json_dict = { "file_location" : "game_file\\" + game_file_location}
    with open(priv_config_fname, "w") as fp:
        json.dump(json_dict, fp)

def main():
    input_fname = input("Type the desired file file name with the .nds extension for your copy of Digimon World Dawn: ")
    init_game_file_folder()
    init_priv_config(input_fname)

if __name__ == "__main__":
    main()