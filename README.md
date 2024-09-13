# _Digimon World Dawn/Dusk_ Autoplayer

Goal
------------
The project aims to create a reinforcement learning agent to play the Nintendo DS (NDS) game _Digimon World: Dawn/Dusk_.

Current Progress
------------
The environment for game playing has been created, which is all ran through `ds_instance_spawners.py`. The project is currently addressing the collection of game data in order to appropriately inform the game agent such as the player location, current story progression, and the stats of different digimon. This is a major roadblock for the project as there are two difficult options for this stage of the project:
* Use template matching as a way to identify game states and locations of necessary game information
* Find the appropriate memory addresses for the necessary game data; an example of this can be found [here](https://projectpokemon.org/home/forums/topic/55238-structure-of-pok%C3%A9mon-in-ram-from-generation-4-games/) with _Pokemon Platinum_

Basic Run
------------
* **Running everything requires DeSmuME to be installed**
* To run:
  ```bash
  $ python -m init_auto_player
  ```
  **NOTE**: You will need to drag your desired .nds file into the created `game_file` folder after running this script.
* Recommended run:
  ```bash
  $ python -m ds_instance_spawners
  ```


Additional Notes
------------
The following keys seem to need the `keymask` to work:
* Directional (up, down, left, right)
* Start/Select Buttons
