"""Handles downloading and installing Notepad++ silently."""

import os
import shutil
import subprocess
import tempfile

import requests


def download_installer(url: str) -> str:
    response = requests.get(url, stream=True)
    response.raise_for_status()
    tmp_dir = tempfile.mkdtemp()
    path = os.path.join(tmp_dir, "npp_installer.exe")
    with open(path, "wb") as f:
        shutil.copyfileobj(response.raw, f)
    return path


def run_installer(installer_path: str) -> None:
    subprocess.run([installer_path, "/S"], check=True)
