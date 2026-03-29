# Python Modules
import ctypes
import sys
from typing import Callable

def is_admin() -> bool:
    """
    Checks if the current user has admin privileges
    :return:
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_as_admin(fn: Callable[[], None] = lambda: None) -> None:
    """
    Runs the app as an administrator.
    """
    if not is_admin():
        print("Requesting Administrator privileges...")
        code = ctypes.windll.shell32.ShellExecuteW(
            None,
            "runas",
            sys.executable,
            " ".join(sys.argv),
            None,
            1
        )
        if code > 32:
            print("Done!")
            sys.exit(0)
        else:
            if code == 5:
                print("Please run the program as administrator.")
            else:
                print(f"UAC request failed with error code: {code}")
    else:
        print("Launching application...")
        fn()


def enable_ansi() -> None:
    """
    Enables ANSI escape code support in legacy Windows consoles.
    """
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.GetStdHandle(-11)
    mode = ctypes.c_uint()
    kernel32.GetConsoleMode(handle, ctypes.byref(mode))
    kernel32.SetConsoleMode(handle, mode.value | 0x0004)