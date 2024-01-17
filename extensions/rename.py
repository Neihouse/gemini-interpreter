import os
import getpass

class RenameExtension:
    def __init__(self):
        self.user = getpass.getuser()

    def open_extension(self):
        print("Rename extension opened.")

    def close_extension(self):
        print("Rename extension closed.")

    def rename_file_or_folder(self, old_name, new_name):
        if self.check_sudo():
            os.rename(old_name, new_name)
            print(f"{old_name} renamed to {newname}.")
        else:
            print("You do not have sudo control.")

    def check_sudo(self):
        return os.geteuid() == 0

rename_extension = RenameExtension()
