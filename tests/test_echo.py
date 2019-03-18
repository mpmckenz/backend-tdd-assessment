#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo


class Test_echo(unittest.TestCase):
    def test_uppercase(self):
        self.assertEqual('-u', 'HELLO WORLD')

    # def test_lowercase(self):
    #     self.assertEqual('-l', 'hello world')

    # def test_title(self):
    #     self.assertEqual('-t', 'Hello World')


if __name__ == '__main__':
    unittest.main()
