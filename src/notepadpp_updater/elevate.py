"""
elevate.py

Provides functions to check and request Administrator privileges on Windows.
"""

import ctypes
import sys


def is_admin() -> bool:
    """
    Check if the current process has Administrator privileges.

    Returns:
        bool: True if running as admin, False otherwise.
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False


def relaunch_as_admin() -> None:
    """
    Relaunch the current script with Administrator privileges, if not already elevated.

    This uses ShellExecuteW with the 'runas' verb, which triggers a UAC prompt.
    """
    if not is_admin():
        print("Re-launching script with Administrator privileges...")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()
