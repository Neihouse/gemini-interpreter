```python
import os
import subprocess

class Copilot:
    def __init__(self):
        self.gemini = None
        self.icon = "copilot_icon"

    def install_dependencies(self):
        dependencies = ["gemini", "copilot", "multimodal", "rename", "create_env", "create_software"]
        for dependency in dependencies:
            subprocess.check_call(["sudo", "apt", "install", "-y", dependency])

    def launch_gemini(self):
        self.gemini = subprocess.Popen(["gemini"], stdout=subprocess.PIPE)

    def open_extension(self, extension_icon):
        if self.gemini:
            os.system(f"xdotool search --onlyvisible --class 'gemini' windowactivate --sync key --clearmodifiers {extension_icon}")

    def write_code(self, code):
        if self.gemini:
            os.system(f"xdotool search --onlyvisible --class 'gemini' windowactivate --sync type --clearmodifiers '{code}'")

if __name__ == "__main__":
    copilot = Copilot()
    copilot.install_dependencies()
    copilot.launch_gemini()
    copilot.open_extension(copilot.icon)
    copilot.write_code("print('Hello, World!')")
```