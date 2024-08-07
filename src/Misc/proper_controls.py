from enum import Enum
from desmume.controls import Keys, keymask

class DSKeys(Enum):
    KEY_A = Keys.KEY_A
    KEY_B = Keys.KEY_B
    KEY_X = Keys.KEY_X
    KEY_Y = Keys.KEY_Y
    KEY_R = Keys.KEY_R
    KEY_L = Keys.KEY_L
    KEY_START = keymask(Keys.KEY_START)
    KEY_SELECT = keymask(Keys.KEY_SELECT)
    NO_KEY_SET = 0xFFFF