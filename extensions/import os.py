import os
import subprocess

class CreateEnvExtension:
    def __init__(self):
        self.user = getpass.getuser()

    def open_extension(self):
        print("CreateEnv extension opened.")

    def close_extension(self):
        print("CreateEnv extension closed.")

    def create_env(self, env_name):
        if self.check_sudo():
            os.makedirs(f"/home/{self.user}/.gemini/envs/{env_name}")
            print(f"Environment {env_name} created.")
        else:
            print("You do not have sudo control.")

    def check_sudo(self):
        return os.geteuid() == 0

create_env_extension = CreateEnvExtension()
