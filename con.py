#!/usr/bin/env python3
"""Convert ANSI colored text into HTML page with customizable colors."""
import sys


def convert():
    """Read text from stdin and convert it to html"""
    for line in sys.stdin:
        print(line)


if __name__ == '__main__':
    convert()
