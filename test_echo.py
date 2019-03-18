import echo
import unittest


class TestEcho(unittest.TestCase):
    parser = echo.create_parser()
    namespace = parser.parse_args(args)

    def test_upper(self):
        args = ['-u', "hEllO woRLd"]
        self.assertTrue(namespace.upper)

        args = ['--upper', "hEllO woRLd"]
        self.assertTrue(namespace.upper)
        self.assertEqual(echo.main(args), "HELLO WORLD")

    def test_lower(self):
        args = ['-l', "hEllO woRLd"]
        self.assertTrue(namespace.lower)

        args = ['--lower', "hEllO woRLd"]
        self.assertTrue(namespace.lower)
        self.assertEqual(echo.main(args), "hello world")

    def test_title(self):
        args = ['-t', "hEllO woRLd"]
        self.assertTrue(namespace.title)

        args = ['--title', "hEllO woRLd"]
        self.assertTrue(namespace.title)
        self.assertEqual(echo.main(args), "Hello World")
