# Project Modules
from ui.display import *
from core.manager import *

# Python Modules
import msvcrt


def main_menu(config: dict) -> dict:
    """
    Displays the main menu and handle the users input.
    :param config: The program configuration.
    :return: The final config.
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
                        if index > 0:
                            index -= 1
                            clear_cmd()
                            show_main_menu(index)
                    case b'P': # Down Arrow
                        if index < 3:
                            index += 1
                            clear_cmd()
                            show_main_menu(index)
                    case _: pass
            if key == b'\r': # Enter key
                match index:
                    case 0:  # Saved configurations
                        pass
                    case 1:  # Create new configuration
                        clear_cmd()
                        config = created_configuration_menu(config)
                        clear_cmd()
                        show_main_menu(index)
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

    return config


#############################
# See current configuration #
#############################

def current_configuration(config: dict) -> None:
    """
    Displays the current configurations and handle the users input.
    :param config: The program configuration.
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
                        if index > 0:
                            index -= 1
                            clear_cmd()
                            show_current_configuration(index, adapters)
                    case b'P': # Down Arrow
                        if index < len(adapters):
                            index += 1
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
    Displays the details of an adapter and handle the users input.
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


############################
# Create new configuration #
############################

def created_configuration_menu(config: dict) -> dict:
    """
    Displays the created network configurations menu and handle the users input.
    :param config: The program configuration.
    :return: The updated program configuration.
    """
    index = 0
    configurations = None
    try:
        configurations = config["configurations"]
    except:
        pass
    if configurations is None or len(configurations) == 0:
        configurations = {}
    clear_cmd()
    show_created_configuration_menu(0, configurations)
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\xe0': # Arrow Key
                arrow = msvcrt.getch()
                match arrow:
                    case  b'H': # Up Arrow
                        if index > 0:
                            index -= 1
                            clear_cmd()
                            show_created_configuration_menu(index, configurations)
                    case b'P': # Down Arrow
                        if index < len(configurations) + 1:
                            index += 1
                            clear_cmd()
                            show_created_configuration_menu(index, configurations)
                    case _: pass
            if key == b'\r': # Enter key
                if index == len(configurations) + 1:
                    break
                pass # TODO

            if key == b'\x1b': # Esc Key
                break

    config["configurations"] = configurations
    return config
