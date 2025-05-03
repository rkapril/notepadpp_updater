"""Handles reading Notepad++ version from Windows Registry."""

import winreg
from typing import Optional, Tuple

REGISTRY_PATHS = [
    (r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Notepad++", "x64"),
    (
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Notepad++",
        "x86",
    ),
]


def get_installed_version() -> Tuple[Optional[str], Optional[str]]:
    for path, arch in REGISTRY_PATHS:
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path) as key:
                display_version, _ = winreg.QueryValueEx(key, "DisplayVersion")
                return display_version, arch
        except FileNotFoundError:
            continue
    return None, None
