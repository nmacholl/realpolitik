import logging
import unittest
from definitions import NAME, VERSION
from realpolitik.command import parse_command
from realpolitik.handlers import DM_COMMAND_HANDLER, CHANNEL_COMMAND_HANDLER

logging.disable(logging.CRITICAL)


class TestCommands(unittest.TestCase):
    def test_parse_command_single(self):
        cmd = '!test'
        parsed, args = parse_command(cmd)
        self.assertIsInstance(parsed, str)
        self.assertIsInstance(args, list)
        self.assertEqual(parsed, 'test')
        self.assertEqual(len(args), 0)

    def test_parse_command_args(self):
        cmd = '!test arg1 arg2'
        parsed, args = parse_command(cmd)
        self.assertIsInstance(parsed, str)
        self.assertIsInstance(args, list)
        self.assertEqual(parsed, 'test')
        self.assertEqual(args, ['arg1', 'arg2'])

    def test_about(self):
        result = DM_COMMAND_HANDLER["about"]()
        self.assertIsInstance(result, str)
        self.assertRegex(result, rf"^{NAME} v{VERSION}")

    def test_help(self):
        result = DM_COMMAND_HANDLER["help"]()
        self.assertIsInstance(result, str)

        for hander in [DM_COMMAND_HANDLER, CHANNEL_COMMAND_HANDLER]:
            for cmd in hander:
                self.assertIn(
                    f" {cmd}", result, f"Command {cmd} is missing from !help output."
                )

    def test_game(self):
        result = CHANNEL_COMMAND_HANDLER["game"]("0")
        print(result)


if __name__ == "__main__":
    unittest.main()
