# Project Modules
from ui.display import *
from core.manager import *

# Python Modules
import msvcrt


def main_menu(config: dict) -> Int:
    """
    Displays the main menu and handle the users input.
    :param config: The program configuration.
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
                        index = index - 1 if index > 0 else 0
                        clear_cmd()
                        show_main_menu(index)
                    case b'P': # Down Arrow
                        index = index + 1 if index < 3 else 3
                        clear_cmd()
                        show_main_menu(index)
                    case _: pass
            if key == b'\r': # Enter key
                match index:
                    case 0:  # Saved configurations
                        pass
                    case 1:  # Create new configuration
                        pass
                    case 2:  # See current configuration
                        clear_cmd()
                        current_configuration(config)
                        clear_cmd()
                        show_main_menu(index)
                    case 3:  # Exit
                        break
                    case _:
                        pass
            if key == b'\x1b': # Esc Key
                break


def current_configuration(config: dict) -> Int:
    """
    Displays the main menu and handle the users input.
    :param config: The program configuration.
    :return: The index of the main menu choice.
    """
    index = 0
    print("Fetching adapters...")
    adapters = list_adapters(config)
    clear_cmd()
    show_current_configuration(index, adapters)
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\xe0': # Arrow Key
                arrow = msvcrt.getch()
                match arrow:
                    case  b'H': # Up Arrow
                        index = index - 1 if index > 0 else 0
                        clear_cmd()
                        show_current_configuration(index, adapters)
                    case b'P': # Down Arrow
                        index = index + 1 if index < len(adapters) else len(adapters)
                        clear_cmd()
                        show_current_configuration(index, adapters)
                    case _: pass
            if key == b'\r': # Enter key
                if index == len(adapters):
                    break
                clear_cmd()
                adapter_details(adapters[index])
                clear_cmd()
                show_current_configuration(index, adapters)
            if key == b'\x1b': # Esc Key
                break


def adapter_details(adapter: wmi.WMIObject = None):
    """
    Displays the details of an adapter.
    :param adapter: The adapter.
    """
    print("Fetching details...")
    clear_cmd()
    details = get_adapter_details(adapter)
    show_adapter_details(details, adapter.Name)
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\x1b':  # Esc Key
                break