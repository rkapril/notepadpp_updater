from unittest.mock import patch

import pytest

from notepadpp_updater import installer


def test_download_installer_invalid_url():
    """Ensure download_installer raises an exception for an invalid or unreachable URL."""

    invalid_url = "http://invalid-url"

    with patch("notepadpp_updater.installer.requests.get") as mock_get:
        mock_get.side_effect = Exception("Failed to download installer")

        with pytest.raises(Exception, match="Failed to download installer"):
            installer.download_installer(invalid_url)
