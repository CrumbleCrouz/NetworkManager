# Project Modules
from ui.display import *
from core.manager import *

# Python Modules
import msvcrt


def main_menu(config: dict) -> dict:
    """
    Displays the main menu and handle the users input.
    :type config: dict
    :param config: The program configuration.
    :return: The final config.
    """
    index = 0
    show_main_menu(index)
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\xe0':  # Arrow Key
                arrow = msvcrt.getch()
                match arrow:
                    case  b'H':  # Up Arrow
                        if index > 0:
                            index -= 1
                            clear_cmd()
                            show_main_menu(index)
                    case b'P':  # Down Arrow
                        if index < 3:
                            index += 1
                            clear_cmd()
                            show_main_menu(index)
                    case _: pass
            if key == b'\r':  # Enter key
                match index:
                    case 0:  # Saved configurations
                        pass
                    case 1:  # Create new configuration
                        clear_cmd()
                        configurations = created_configuration_menu(config)
                        config["configurations"] = configurations
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
            if key == b'\x1b':  # Esc Key
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
            if key == b'\xe0':  # Arrow Key
                arrow = msvcrt.getch()
                match arrow:
                    case  b'H':  # Up Arrow
                        if index > 0:
                            index -= 1
                            clear_cmd()
                            show_current_configuration(index, adapters)
                    case b'P':  # Down Arrow
                        if index < len(adapters):
                            index += 1
                            clear_cmd()
                            show_current_configuration(index, adapters)
                    case _: pass
            if key == b'\r':  # Enter key
                if index == len(adapters):
                    break
                clear_cmd()
                adapter_details(adapters[index])
                clear_cmd()
                show_current_configuration(index, adapters)
            if key == b'\x1b':  # Esc Key
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

def created_configuration_menu(config: dict) -> list:
    """
    Displays the created network configurations menu and handle the users input.
    :param config: The program configuration.
    :return: The updated network configurations.
    """
    index = 0
    configurations = None
    try:
        configurations = config["configurations"]
    except:
        pass
    if configurations is None:
        configurations = []
    clear_cmd()
    show_created_configuration_menu(0, configurations)
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\xe0':  # Arrow Key / Del
                arrow = msvcrt.getch()
                match arrow:
                    case  b'H':  # Up Arrow
                        if index > 0:
                            index -= 1
                            clear_cmd()
                            show_created_configuration_menu(index, configurations)
                    case b'P':  # Down Arrow
                        if index < len(configurations) + 1:
                            index += 1
                            clear_cmd()
                            show_created_configuration_menu(index, configurations)
                    case b'S':  # Delete Key
                        if index < len(configurations):
                            print("Are you sure to delete this configuration ?")
                            if input("Type \"yes\" to confirm: ") == "yes":
                                configurations.pop(index)
                                clear_cmd()
                                show_created_configuration_menu(index, configurations)
                                print("Successfully deleted!")
                            clear_cmd()
                            show_created_configuration_menu(index, configurations)
                            print("Aborted.")
                    case _: pass
            if key == b'\r':  # Enter key
                if index == len(configurations) + 1:  # Go Back
                    break
                if index == len(configurations):  # Create new configuration
                    new_config = create_or_edit_configuration(configurations)
                    clear_cmd()
                    show_created_configuration_menu(index, configurations)
                    if new_config is not None:
                        configurations.append(new_config)
                        clear_cmd()
                        show_created_configuration_menu(index, configurations)
                        print("Successfully created!")
                    else:
                        print("Aborted.")
                else:  # Edit configuration
                    updated_configuration = create_or_edit_configuration(configurations, configurations[index].copy(), False, index)
                    clear_cmd()
                    show_created_configuration_menu(index, configurations)
                    if updated_configuration is not None:
                        if len(updated_configuration.keys()) > 0:
                            configurations[index] = updated_configuration
                            clear_cmd()
                            show_created_configuration_menu(index, configurations)
                            print("Successfully updated!")
                        else:
                            configurations.pop(index)
                            clear_cmd()
                            show_created_configuration_menu(index, configurations)
                            print("Successfully deleted!")
                    else:
                        print("Aborted.")

            if key == b'\x1b':  # Esc Key
                break
    return configurations


def create_or_edit_configuration(configurations: list, configuration: dict = None, create: bool = True, config_index:int = 0) -> dict | None:
    """
    Displays the menu to create or update network configuration and handle the users input.
    :param configurations: All the network configurations, used to verify name uniqueness.
    :param configuration: The network configuration to update.
    :param create: True if the user is creating a new configuration,
                   False if the user is editing an existent configuration.
   :param config_index: The index of the configuration in the configurations list.
    :return: The created / updated configuration or None if aborted.
    """
    if configuration is None:
        configuration = {
            "Name": "New Configuration",
            "DHCP": False,
            "IP": None,
            "Mask": None,
            "Gateway": None,
            "DNS": []
        }
    index = 0
    clear_cmd()
    show_create_or_edit_configuration(0, configuration, create)
    while True:
        if configuration["DHCP"]:
            max_index = 3 + (1 if not create else 0)
        else:
            max_index = len(configuration.keys()) + len(configuration["DNS"]) + 1 + (1 if not create else 0)
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\xe0':  # Arrow Key
                arrow = msvcrt.getch()
                match arrow:
                    case  b'H':  # Up Arrow
                        if index > 0:
                            index -= 1
                            clear_cmd()
                            show_create_or_edit_configuration(index, configuration, create)
                    case b'P':  # Down Arrow
                        if index < max_index:
                            index += 1
                            clear_cmd()
                            show_create_or_edit_configuration(index, configuration, create)
                    case _: pass

            if key == b'\r':  # Enter key
                if index == 0:  # Name
                    name = input("Enter new Name: ")
                    clear_cmd()
                    show_create_or_edit_configuration(index, configuration, create)
                    if name == "":
                        print("Name cannot be empty!")
                        continue
                    elif len(name) > 64:
                        print("Name cannot be longer than 64 characters!")
                        continue
                    elif len(configurations) > 0:
                        if name.lower() in ([n["Name"].lower() for n in configurations]):
                            print("A configuration with this name already exists!")
                            continue
                    configuration["Name"] = name
                    clear_cmd()
                    show_create_or_edit_configuration(index, configuration, create)
                    print("Name updated!")
                if (not configuration["DHCP"]) and index == 1:  # IP
                    ip = input("Enter new IP: ")
                    clear_cmd()
                    show_create_or_edit_configuration(index, configuration, create)
                    if ip == "":
                        print("IP cannot be empty!")
                    elif verify_ip(ip):
                        configuration["IP"] = ip
                        clear_cmd()
                        show_create_or_edit_configuration(index, configuration, create)
                        print("IP updated!")
                    else:
                        print("Invalid IP!")
                if (not configuration["DHCP"]) and index == 2:  # Mask
                    mask = input("Enter new Mask: ")
                    clear_cmd()
                    show_create_or_edit_configuration(index, configuration, create)
                    if mask == "":
                        print("Mask cannot be empty!")
                    elif verify_ip(mask):
                        configuration["Mask"] = mask
                        clear_cmd()
                        show_create_or_edit_configuration(index, configuration, create)
                        print("Mask updated!")
                    else:
                        print("Invalid Mask!")
                if (not configuration["DHCP"]) and index == 3:  # Gateway
                    gateway = input("Enter new Gateway (can be None): ")
                    clear_cmd()
                    show_create_or_edit_configuration(index, configuration, create)
                    if gateway == "" or gateway == "None":
                        configuration["Gateway"] = None
                        clear_cmd()
                        show_create_or_edit_configuration(index, configuration, create)
                        print("Gateway updated!")
                    elif verify_ip(gateway):
                        configuration["Gateway"] = gateway
                        clear_cmd()
                        show_create_or_edit_configuration(index, configuration, create)
                        print("Gateway updated!")
                    else:
                        print("Invalid IP!")
                if (not configuration["DHCP"]) and index in range(4, max_index - (3 if (not create) else 2)):  # DNS
                    if index == max_index - (4 if (not create) else 3):  # Add DNS
                        dns = input("Enter new DNS: ")
                        clear_cmd()
                        show_create_or_edit_configuration(index, configuration, create)
                        if dns == "":
                            print("DNS cannot be empty!")
                        elif verify_ip(dns):
                            configuration["DNS"].append(dns)
                            clear_cmd()
                            show_create_or_edit_configuration(index, configuration, create)
                            print("DNS added!")
                        else:
                            print("Invalid DNS!")
                    else:  # Edit DNS
                        dns_index = index - 4
                        dns = input(f"Edit DNS {configuration["DNS"][dns_index]}: ")
                        clear_cmd()
                        show_create_or_edit_configuration(index, configuration, create)
                        if dns == "":
                            print("DNS cannot be empty!")
                        elif verify_ip(dns):
                            configuration["DNS"][dns_index] = dns
                            clear_cmd()
                            show_create_or_edit_configuration(index, configuration, create)
                            print("DNS updated!")
                        else:
                            print("Invalid DNS!")

                if index == max_index - (3 if (not create) else 2):  # DHCP
                    configuration["DHCP"] = not configuration["DHCP"]
                    clear_cmd()
                    if configuration["DHCP"]:
                        index = 1
                    else:
                        index = len(configuration.keys()) + len(configuration["DNS"]) -1
                    show_create_or_edit_configuration(index, configuration, create)
                    print("DHCP updated")
                if index == max_index - (2 if (not create) else 1):  # Validate
                    print("Would you want to save the configuration ?")
                    if input("Type \"yes\" to confirm: ") == "yes":
                        if len(configurations) > 0:
                            config_name_list = [n["Name"].lower() for n in configurations]
                            config_name_list.pop(config_index)
                            if configuration["Name"].lower() in config_name_list:
                                print("A configuration with this name already exists!")
                                continue
                        if verify_configuration(configuration):
                            return configuration
                        else:
                            clear_cmd()
                            show_create_or_edit_configuration(index, configuration, create)
                            print("Cannot validate, invalid configuration!")
                    else:
                        clear_cmd()
                        show_create_or_edit_configuration(index, configuration, create)
                        print("Aborted.")
                if (not create) and index == max_index - 1:  # Delete
                    print("Are you sure to delete this configuration ?")
                    if input("Type \"yes\" to confirm: ") == "yes":
                        return {}
                    clear_cmd()
                    show_create_or_edit_configuration(index, configuration, create)
                    print("Aborted.")
                if index == max_index:  # Go back
                    print("Would you want to discard your changes ?")
                    if input("Type \"yes\" to confirm: ") == "yes":
                        break
                    clear_cmd()
                    show_create_or_edit_configuration(index, configuration, create)
                    print("Aborted.")

            if key == b'\x1b':  # Esc Key
                print("Would you want to discard your changes ?")
                if input("Type \"yes\" to confirm: ") == "yes":
                    break
                clear_cmd()
                show_create_or_edit_configuration(index, configuration, create)
                print("Aborted.")

    return None
