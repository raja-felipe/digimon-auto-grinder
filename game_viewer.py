import numpy as np
import cv2
from win32gui import GetWindowRect, FindWindow, EnumWindows, IsWindowVisible, GetWindowText
from mss import mss
from PIL import Image
import json


def extract_ds_window():
    with open("config.json", "r") as fp:
        config = json.load(fp)
        window_name = config["ds_window"]

    ds_window = FindWindow(None, window_name)
    window_rect = GetWindowRect(ds_window)
    print(window_rect)

    return window_rect

def show_ds_player():

    sct = mss()

    window_bounds = extract_ds_window()
    bounding_box = {
        "left": window_bounds[0],
        "top" : window_bounds[1],
        "width": window_bounds[2],
        "height": window_bounds[3]
        }
    
    print(bounding_box)

    while True:

        sct_img = sct.grab(bounding_box)
        cv2.imshow('screen', np.array(sct_img))

        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            cv2.destroyAllWindows()
            break
    return

def winEnumHandler( hwnd, ctx ):
    if IsWindowVisible( hwnd ):
        print ( hex( hwnd ), GetWindowText( hwnd ) )
    return

def main():
    EnumWindows( winEnumHandler, None )
    show_ds_player()
    return

if __name__ == "__main__":
    main()