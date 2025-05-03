from unittest.mock import patch

from notepadpp_updater import updater


def test_get_latest_release_structure_mocked():
    """Test get_latest_release with mocked GitHub response."""
    fake_response = {
        "tag_name": "v8.6.2",
        "assets": [
            {
                "name": "npp.8.6.2.Installer.x64.exe",
                "browser_download_url": "https://example.com/npp.exe",
            }
        ],
    }

    with patch("notepadpp_updater.updater.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = fake_response

        version, url = updater.get_latest_release("x64")

        assert version == "8.6.2"
        assert url == "https://example.com/npp.exe"
