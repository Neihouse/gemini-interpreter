```python
import os
import subprocess
from extensions import copilot, multimodal, rename, create_env, create_software

class Gemini:
    def __init__(self):
        self.extensions = {
            "copilot": copilot.Copilot(),
            "multimodal": multimodal.Multimodal(),
            "rename": rename.Rename(),
            "create_env": create_env.CreateEnv(),
            "create_software": create_software.CreateSoftware()
        }

    def launch(self):
        print("Launching Gemini Terminal...")
        self.open_extension("copilot")

    def open_extension(self, extension_name):
        if extension_name in self.extensions:
            self.extensions[extension_name].open()
        else:
            print(f"Extension {extension_name} not found.")

    def close_extension(self, extension_name):
        if extension_name in self.extensions:
            self.extensions[extension_name].close()
        else:
            print(f"Extension {extension_name} not found.")

    def sudo_control(self, command):
        subprocess.run(['sudo', command], check=True)

if __name__ == "__main__":
    gemini = Gemini()
    gemini.launch()
```