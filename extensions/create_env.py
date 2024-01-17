```python
import os
import subprocess

class CreateEnvExtension:
    def __init__(self, gemini_terminal):
        self.gemini_terminal = gemini_terminal

    def open_extension(self):
        self.gemini_terminal.open_extension('Create Env')

    def close_extension(self):
        self.gemini_terminal.close_extension('Create Env')

    def create_env(self, env_name):
        command = f'sudo virtualenv {env_name}'
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        process.wait()
        if process.returncode == 0:
            print(f'Environment {env_name} created successfully.')
        else:
            print(f'Failed to create environment {env_name}.')

    def interact_with_extension(self, env_name):
        self.open_extension()
        self.create_env(env_name)
        self.close_extension()
```