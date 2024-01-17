import os
import subprocess

def install_dependencies():
  # Install the Gemini terminal emulator.
  subprocess.run(['sudo', 'apt-get', 'install', 'gemini-terminal-emulator'])

  # Install the extension interface.
  subprocess.run(['sudo', 'apt-get', 'install', 'extension-interface'])

  # Install sudo control.
  subprocess.run(['sudo', 'apt-get', 'install', 'sudo'])

  # Install the file and folder names.
  subprocess.run(['sudo', 'apt-get', 'install', 'file-and-folder-names'])

  # Install the environment names.
  subprocess.run(['sudo', 'apt-get', 'install', 'environment-names'])

  # Install the software names.
  subprocess.run(['sudo', 'apt-get', 'install', 'software-names'])

  # Install the DOM elements.
  subprocess.run(['sudo', 'apt-get', 'install', 'dom-elements'])

  # Install the message names.
  subprocess.run(['sudo', 'apt-get', 'install', 'message-names'])

  # Install the function names.
  subprocess.run(['sudo', 'apt-get', 'install', 'function-names'])

if __name__ == "__main__":
  install_dependencies()
