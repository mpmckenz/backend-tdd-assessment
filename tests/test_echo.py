#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Michael McKenzie"

import echo
import unittest
import subprocess


class TestEcho(unittest.TestCase):

    def test_help(self):
        """Running the program without arguments should show usage."""
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()
        print stdout
        print usage
        self.assertEquals(stdout, usage)

    def test_upper(self):
        args = ['-u', "hEllO woRLd"]
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        self.assertTrue(namespace.upper)
        args = ['--upper', "hEllO woRLd"]
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        self.assertTrue(namespace.upper)
        self.assertEqual(echo.main(args), "HELLO WORLD")

    def test_lower(self):
        args = ['-l', "hEllO woRLd"]
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        self.assertTrue(namespace.lower)
        args = ['--lower', "hEllO woRLd"]
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        self.assertTrue(namespace.lower)
        self.assertEqual(echo.main(args), "hello world")

    def test_title(self):
        args = ['-t', "hEllO woRLd"]
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        self.assertTrue(namespace.title)
        args = ['--title', "hEllO woRLd"]
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        self.assertTrue(namespace.title)
        self.assertEqual(echo.main(args), "Hello World")

    def test_no_args(self):
        args = ['heLLo!']
        self.assertEquals(echo.main(args), 'heLLo!')

    def test_all_args(self):
        args = ['-tul', 'heLLo!']
        self.assertEquals(echo.main(args), 'Hello!')


if __name__ == '__main__':
    unittest.main()
