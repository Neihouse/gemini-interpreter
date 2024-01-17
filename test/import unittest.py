import unittest

from create_software import CreateSoftwareExtension


class TestCreateSoftwareExtension(unittest.TestCase):

    def setUp(self):
        self.create_software_extension = CreateSoftwareExtension()

    def test_set_software_name(self):
        self.create_software_extension.set_software_name('test_software')
        self.assertEqual(self.create_software_extension.software_name, 'test_software')

    def test_create_software(self):
        self.create_software_extension.set_software_name('test_software')
        self.create_software_extension.create_software()
        self.assertTrue(os.path.exists('/usr/bin/test_software'))

    def test_open_extension(self):
        self.create_software_extension.open_extension()
        # Placeholder for testing the opening of the extension in the Gemini terminal

    def test_close_extension(self):
        self.create_software_extension.close_extension()
        # Placeholder for testing the closing of the extension in the Gemini terminal


if __name__ == '__main__':
    unittest.main()
