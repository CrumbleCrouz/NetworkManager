# Python Modules
import json
from pathlib import Path


def load_config() -> dict:
    """
    Loads config file
    :return: the loaded config
    """
    config_path = Path(__file__).parent.parent.absolute() / "config.json"
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        return {}


def save_config(config: dict) -> None:
    """
    Saves config file
    :param config: The program config
    """
    config_path = Path(__file__).parent.parent.absolute() / "config.json"
    try:
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=4)
    except Exception as e:
        print(f"Unable to save config.json: {e}")