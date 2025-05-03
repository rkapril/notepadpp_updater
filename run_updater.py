from src.notepadpp_updater import elevate, updater

if __name__ == "__main__":
    elevate.relaunch_as_admin()
    updater.update_if_needed()
    input("\nPress Enter to exit...")
