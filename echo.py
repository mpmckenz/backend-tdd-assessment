#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "Michael McKenzie"


import sys
import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    parser.add_argument(
        "-u", "--upper", help="convert text to uppercase", action="store_true")
    parser.add_argument('string', help='enter your string')
    parser.add_argument(
        "-l", "--lower", help="convert text to lowercase", action="store_true")
    parser.add_argument(
        "-t", "--title", help="convert text to titlecase", action="store_true")
    # parser.add_argument(
    # "-h", "--help", help="", action="store_true")
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    namespace = parser.parse_args(args)
    if namespace.upper:
        namespace.string = namespace.string.upper()
    elif namespace.lower:
        namespace.string = namespace.string.lower()
    elif namespace.title:
        namespace.string = namespace.string.title()
    return namespace.string


if __name__ == '__main__':
    print main(sys.argv[1:])
