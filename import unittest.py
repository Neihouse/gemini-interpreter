import unittest

from gemini import Gemini


class TestGemini(unittest.TestCase):

    def setUp(self):
        self.gemini = Gemini()

    def test_main_loop(self):
        self.gemini.main_loop()

    def test_parse_input(self):
        self.assertEqual(self.gemini.parse_input("echo hello world"), ["echo", "hello", "world"])

    def test_execute_input(self):
        self.gemini.execute_input(["echo", "hello", "world"])
        self.assertEqual(self.gemini.output, "hello world\n")

    def test_open_extension(self):
        self.gemini.open_extension("copilot")
        self.assertTrue(self.gemini.copilot.is_open())

    def test_close_extension(self):
        self.gemini.open_extension("copilot")
        self.gemini.close_extension("copilot")
        self.assertFalse(self.gemini.copilot.is_open())

    def test_sudo_control(self):
        self.gemini.sudo_control("echo hello world")
        self.assertEqual(self.gemini.output, "hello world\n")

    def test_add_feature(self):
        self.gemini.add_feature("run_code_in_different_languages")
        self.assertTrue(self.gemini.has_feature("run_code_in_different_languages"))

    def test_add_run_code_in_different_languages_feature(self):
        self.gemini.add_run_code_in_different_languages_feature()
        self.assertTrue(self.gemini.has_feature("run_code_in_different_languages"))

    def test_add_debug_code_feature(self):
        self.gemini.add_debug_code_feature()
        self.assertTrue(self.gemini.has_feature("debug_code"))

    def test_add_unit_test_code_feature(self):
        self.gemini.add_unit_test_code_feature()
        self.assertTrue(self.gemini.has_feature("unit_test_code"))

    def test_add_deploy_code_to_production_feature(self):
        self.gemini.add_deploy_code_to_production_feature()
        self.assertTrue(self.gemini.has_feature("deploy_code_to_production"))


if __name__ == "__main__":
    unittest.main()
