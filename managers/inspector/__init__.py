from time import sleep

import keyboard
from pyautogui import position


def start_mouse_inspector():
    click_positions = []
    while True:
        if keyboard.is_pressed('0'):
            current_position = position()
            click_positions.append({
                'x': current_position.x,
                'y': current_position.y
            })
            sleep(0.2)
        if keyboard.is_pressed('esc'):
            return click_positions
