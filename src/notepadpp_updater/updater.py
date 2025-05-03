"""Coordinates checking and updating Notepad++."""

import requests
from packaging import version

from .installer import download_installer, run_installer
from .registry import get_installed_version

NPP_GITHUB_RELEASES = (
    "https://api.github.com/repos/notepad-plus-plus/notepad-plus-plus/releases/latest"
)


def get_latest_release(arch: str) -> tuple[str, str]:
    resp = requests.get(NPP_GITHUB_RELEASES, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    suffix = "Installer.x64.exe" if arch == "x64" else "Installer.exe"
    for asset in data["assets"]:
        if asset["name"].endswith(suffix):
            return data["tag_name"].lstrip("v"), asset["browser_download_url"]
    raise RuntimeError("Suitable installer not found.")


def update_if_needed() -> None:
    installed_ver, arch = get_installed_version()
    arch = arch or "x64"

    latest_ver, url = get_latest_release(arch)

    if installed_ver and version.parse(installed_ver) >= version.parse(latest_ver):
        print("Notepad++ is up to date.")
        return

    print(f"Updating Notepad++ from {installed_ver or 'not installed'} to {latest_ver}")
    installer = download_installer(url)
    run_installer(installer)
    print("Updating completed.")
