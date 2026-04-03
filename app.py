# Project Modules
from core.utils import *
from core.serialization import *
from ui.controllers import *

# Python Modules
import os


def main():
    """
    Main function.
    """
    enable_ansi()
    clear_cmd()
    config = load_config()
    main_menu(config)
    save_config(config)


if __name__ == "__main__":
    try:
        run_as_admin(main)

    except KeyboardInterrupt:
        pass
    finally:
        print("Exiting program...")
        os.system("pause")
