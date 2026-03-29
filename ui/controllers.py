# Project Modules
from ui.display import show_main_menu, clear_cmd

# Python Modules
import msvcrt


def main_menu() -> Int:
    """
    Displays the main menu and handle the users input.
    :return: The index of the main menu choice.
    """
    index = 0
    show_main_menu(index)
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\xe0': # Arrow Key
                arrow = msvcrt.getch()
                match arrow:
                    case  b'H': # Up Arrow
                        index = 0
                        clear_cmd()
                        show_main_menu(index)
                    case b'P': # Down Arrow
                        index = 1
                        clear_cmd()
                        show_main_menu(index)
                    case _: pass
            if key == b'\r': # Enter key
                return index
            if key == b'\x1b': # Esc Key
                break
