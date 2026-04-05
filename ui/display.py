


def clear_cmd() -> None:
    """
    Clears the screen.
    """
    print("\033[H\033[J", end="")


def show_main_menu(index: int = 0) -> None:
    """
    Displays the main menu.
    :param index: Starting index.
    """
    print(f"╔═════╦═══════════════════════════╗")
    print(f"║ [{'x' if index == 0 else ' '}] ║ Saved configurations      ║ - Not implemented yet -")
    print(f"║ [{'x' if index == 1 else ' '}] ║ Create new configuration  ║ - Not implemented yet -")
    print(f"║ [{'x' if index == 2 else ' '}] ║ See current configuration ║")
    print(f"║ [{'x' if index == 3 else ' '}] ║ Exit                      ║")
    print(f"╚═════╩═══════════════════════════╝")


def show_current_configuration(index: int = 0, adapters: list = []) -> None:
    """
    Displays the current configurations.
    :param index: Starting index.
    :param adapters: A list containing all adapters.
    """
    max_name_length = max(len(adapter.Name) for adapter in adapters)
    max_name_length = max(max_name_length, 7)  # 7 is the length of "Go back"
    print(f"╔═════╦═{'═' * max_name_length}═╗")
    c = 0
    for adapter in adapters:
        print(f"║ [{'x' if index == c else ' '}] ║ {adapter.Name + ' ' * (max_name_length - len(adapter.Name))} ║")
        c += 1
    print(f"║ [{'x' if index == c else ' '}] ║ Go back{ ' ' * (max_name_length - 7)} ║")
    print(f"╚═════╩═{'═' * max_name_length}═╝")


def show_adapter_details(details: dict = None, name: str = "") -> None:
    """
    Displays the adapter details.
    :param details: Details of the adapter.
    :param name: Name of the adapter.
    """
    if details is None:
        details = {}
    caution_1 = "\"N/A\" might indicate a non-existent"
    caution_2 = "connection, or undefined values"
    go_back = "Press Esc to go back"
    name_length = len(name)
    max_value_length = max(len(v) for v in details.values())
    max_length = max(name_length, max_value_length, len(caution_1))
    print(f"╔═{'═' * 7}═╦═{(' ' + name + ' ').center(max_length + 2, '═')}═╗")
    for (k, v) in details.items():
        print(f"║ {k:<7} ║ {v:<{max_length + 2}} ║")
    print(f"╠═{'═' * 7}═╩═{'═' * (max_length + 2)}═╣")
    print(f"║ {caution_1.center(12 + max_length)} ║")
    print(f"║ {caution_2.center(12 + max_length)} ║")
    print(f"║ {''.center(12 + max_length)} ║")
    print(f"║ {go_back.center(12 + max_length)} ║")
    print(f"╚═{'═' * (12 + max_length)}═╝")


def show_created_configuration_menu(index: int = 0, configurations: dict = None):
    """
    Displays the saved configurations.
    :param configurations: The saved configurations.
    """

    if configurations is None:
        configurations = {}
    indication_1 = "Select a created configuration"
    indication_2 = "will edit it"
    max_length = max(len(config["name"]) for config in configurations) if len(configurations) > 0 else 0
    max_length = max(max_length, len(indication_1), len(indication_2), 24)  # 24 is the length of "Create new configuration"
    print(f"╔═════╦═{'═' * max_length}═╗")
    c = 0
    for config in configurations:
        print(
            f"║ [{'x' if index == c else ' '}] ║ {config["name"] + ' ' * (max_length - len(config["name"]))} ║")
        c += 1
    print(f"║ [{'x' if index == c else ' '}] ║ Create new configuration{' ' * (max_length - 24)} ║")
    print(f"║ [{'x' if index == c + 1 else ' '}] ║ Go back{' ' * (max_length - 7)} ║")
    print(f"╠═{'═' * 3}═╩═{'═' * max_length}═╣")
    print(f"║ {indication_1.center(6 + max_length)} ║")
    print(f"║ {indication_2.center(6 + max_length)} ║")
    print(f"║ {''.center(6 + max_length)} ║")
    print(f"╚═{'═' * (max_length + 6)}═╝")
    # ╔ ╗ ═ ║ ╠ ╦ ╬ ╩ ╣ ╚ ╝
