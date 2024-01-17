import os
import subprocess

class ExtensionInterface:
    def __init__(self):
        self.extensions = {}

    def register_extension(self, extension_name, extension_class):
        self.extensions[extension_name] = extensionclass

    def open_extension(self, extension_name):
        if extension_name in self.extensions:
            self.extensions[extensionname].open_extension()
        else:
            print(f"Extension {extension_name} not found.")

    def close_extension(self, extension_name):
        if extension_name in self.extensions:
            self.extensions[extensionname].close_extension()
        else:
            print(f"Extension {extension_name} not found.")

    def get_extension(self, extension_name):
        if extension_name in self.extensions:
            return self.extensions[extensionname]
        else:
            return None

    def get_all_extensions(self):
        return self.extensions.keys()

extension_interface = ExtensionInterface()
