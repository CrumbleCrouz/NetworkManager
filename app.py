# Project Modules
from core.manager import list_physical_adapters
from core.utils import *
from core.serialization import *
from ui.controllers import *

# Python Modules
import os


def main():
    """
    Main function
    """
    enable_ansi()
    clear_cmd()
    config = load_config()
    while True:
        main_menu()
        list_physical_adapters(config)
        break
    save_config(config)
    os.system("pause")


if __name__ == "__main__":
    run_as_admin(main)