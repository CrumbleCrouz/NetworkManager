def clear_cmd() -> None:
    """
        Clears the screen
    """
    print("\033[H\033[J", end="")


def show_main_menu(index: int = 0) -> None:
    # ╔ ╗ ═ ║ ╠ ╦ ╬ ╩ ╣ ╚ ╝
    print(f"╔═════╦══════════════════════╗")
    print(f"║ [{'x' if index == 0 else ' '}] ║ Saved Configurations ║")
    print(f"║ [{'x' if index == 1 else ' '}] ║ Enter Manualy        ║")
    print(f"╚═════╩══════════════════════╝")
