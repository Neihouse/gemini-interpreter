```python
import os
import shutil
from gemini import Gemini, Extension

class Multimodal(Extension):
    def __init__(self, gemini):
        super().__init__(gemini)
        self.icon = "multimodal_icon"

    def open(self):
        super().open()
        print("Multimodal extension is now open.")

    def close(self):
        super().close()
        print("Multimodal extension is now closed.")

    def organize_files(self, source, destination):
        if self.is_open and self.gemini.sudo:
            try:
                shutil.move(source, destination)
                print(f"Moved {source} to {destination}")
            except Exception as e:
                print(f"Error moving file: {e}")
        else:
            print("Please open the Multimodal extension and ensure you have sudo permissions.")

    def organize_folders(self, source, destination):
        if self.is_open and self.gemini.sudo:
            try:
                shutil.move(source, destination)
                print(f"Moved {source} to {destination}")
            except Exception as e:
                print(f"Error moving folder: {e}")
        else:
            print("Please open the Multimodal extension and ensure you have sudo permissions.")

if __name__ == "__main__":
    gemini = Gemini()
    multimodal = Multimodal(gemini)
    gemini.add_extension(multimodal)
```