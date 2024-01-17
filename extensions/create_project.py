import os
import subprocess
from extensions import copilot, multimodal, rename, create_env, create_software

class CreateProjectExtension:
    def __init__(self):
        # Initialize any necessary variables or settings for the extension
        self.colab = copilot.Copilot()
        self.multimodal = multimodal.Multimodal()
        self.rename = rename.Rename()
        self.create_env = create_env.CreateEnv()
        self.create_software = create_software.CreateSoftware()

    def open_extension(self):
        # Code to open the Create Project extension in the Gemini terminal
        self.colab.open()
        self.multimodal.open()
        self.rename.open()
        self.create_env.open()
        self.create_software.open()

    def close_extension(self):
        # Code to close the Create Project extension in the Gemini terminal
        self.colab.close()
        self.multimodal.close()
        self.rename.close()
        self.create_env.close()
        self.create_software.close()

    def create_new_project(self, project_name, project_type):
        # Code to create a new software project
        # Placeholder for the actual implementation
        pass

