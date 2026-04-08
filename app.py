# Project Modules
from core.utils import *
from core.serialization import *
from ui.controllers import *


def main():
    """
    Main function.
    """
    enable_ansi()
    clear_cmd()
    config = load_config()
    try:
        config = main_menu(config)
    except KeyboardInterrupt:
        pass
    finally:
        save_config(config)
        print("Exiting program...")


if __name__ == "__main__":
    run_as_admin(main)
