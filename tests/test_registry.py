from unittest.mock import MagicMock, patch

from notepadpp_updater.registry import get_installed_version


def test_get_installed_version_mock_installed():
    """Simulate Notepad++ installed (mocking registry values)."""

    mock_key = MagicMock()

    with patch(
        "notepadpp_updater.registry.winreg.OpenKey", return_value=mock_key
    ), patch(
        "notepadpp_updater.registry.winreg.QueryValueEx", return_value=("8.6.2", None)
    ):

        version, arch = get_installed_version()

        assert version == "8.6.2"
        assert (
            arch == "x64"
        )  # Based on registry path logic if you're detecting arch from it
