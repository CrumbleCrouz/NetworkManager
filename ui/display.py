


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
    print(f"║ [{'x' if index == 1 else ' '}] ║ Manage configuration      ║ - Working on it -")
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


def show_created_configuration_menu(index: int = 0, configurations: list = None) -> None:
    """
    Displays the saved configurations.
    :param index: Starting index.
    :param configurations: The saved configurations.
    """
    if configurations is None:
        configurations = []
    create_config = "Create new configuration"
    indication_1 = "Select a created configuration"
    indication_2 = "will edit it"
    go_back = "Go back"
    max_length = max(len(config["Name"]) for config in configurations) if len(configurations) > 0 else 0
    max_length = max(max_length, len(indication_1), len(indication_2), len(create_config))
    print(f"╔═════╦═{'═' * max_length}═╗")
    c = 0
    for config in configurations:
        print(
            f"║ [{'x' if index == c else ' '}] ║ {config["Name"] + ' ' * (max_length - len(config["Name"]))} ║")
        c += 1
    print(f"║ [{'x' if index == c else ' '}] ║ {create_config + ' ' * (max_length - len(create_config))} ║")
    print(f"║ [{'x' if index == c + 1 else ' '}] ║ {go_back + ' ' * (max_length - len(go_back))} ║")
    print(f"╠═{'═' * 3}═╩═{'═' * max_length}═╣")
    print(f"║ {indication_1.center(6 + max_length)} ║")
    print(f"║ {indication_2.center(6 + max_length)} ║")
    print(f"╚═{'═' * (max_length + 6)}═╝")


def show_create_or_edit_configuration(index: int = 0, configuration: dict = None, create: bool = True) -> None:
    """
    Displays the saved configurations.
    :param index: Starting index.
    :param configuration: The new configuration.
    :param create: True if the user is creating a new configuration,
                   False if the user is editing an existent configuration.
    """
    go_back = "Go back"
    validate = "Create new Configuration" if create else "Update Configuration"
    add_dns = "create new DNS server"
    indication_1 = "Type Enter to edit the selected field"
    indication_2 = "Going back will not save changes"
    dns_length = sum(len(dns) for dns in configuration["DNS"])
    max_length = max((len(str(configuration[prop])) for prop in configuration.keys() if prop != "DNS"), default=0)
    max_length = max(
        max_length,
        dns_length,
        len(go_back),
        len(validate),
        len(add_dns),
        len(indication_1),
        len(indication_2),
        len(configuration["Name"])
        )
    print(f"╔═════╦═{(' ' + configuration["Name"] + ' ').center(max_length, '═')}═╗")
    print(f"║ [{'x' if index == 0 else ' '}] ║ Name: {configuration["Name"] + ' ' * (max_length - len(configuration["Name"]) - 6)} ║")
    c = 1
    if not configuration["DHCP"]:
        for prop in configuration.keys():
            if prop not in ["Name", "DHCP", "DNS"]:
                print(f"║ [{'x' if index == c else ' '}] ║ {(prop)}: {str(configuration[prop]) + ' ' * (max_length - len(str(configuration[prop])) - len(prop) - 2)} ║")
                c += 1
            elif prop is "DNS":
                print(f"║     ║ {prop}: {' ' * (max_length - len(prop) - 2)} ║")
                for srv in configuration[prop]:
                    print(f"║ [{'x' if index == c else ' '}] ║  - {srv + ' ' * (max_length - len(srv) - 3)} ║")
                    c += 1
                print(f"║ [{'x' if index == c else ' '}] ║  - {add_dns + ' ' * (max_length - len(add_dns) - 3)} ║")
                c += 1
    print(f"║ [{'x' if index == c else ' '}] ║ DHCP: {str(configuration["DHCP"]) + ' ' * (max_length - len(str(configuration["DHCP"])) - 6)} ║")
    print(f"║ [{'x' if index == c + 1 else ' '}] ║ {validate + ' ' * (max_length - len(validate))} ║")
    print(f"║ [{'x' if index == c + 2 else ' '}] ║ {go_back + ' ' * (max_length - len(go_back))} ║")

    print(f"╠═{'═' * 3}═╩═{'═' * max_length}═╣")
    print(f"║ {indication_1.center(6 + max_length)} ║")
    print(f"║ {indication_2.center(6 + max_length)} ║")
    print(f"║ {''.center(6 + max_length)} ║")
    print(f"╚═{'═' * (max_length + 6)}═╝")
    # ╔ ╗ ═ ║ ╠ ╦ ╬ ╩ ╣ ╚ ╝
