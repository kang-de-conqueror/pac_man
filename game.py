#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Preliminaries of PacMan Game"""

import logging

# Set logging
logging.basicConfig(level=logging.ERROR, filemode='w')


def load_map(file_pathname):
    """Load Pac-Man Map

    Arguments:
        file_pathname {str} -- the file path name of a Pac-Man map

    Raises:
        FileNotFoundError: Provided file path name is not found
        IOError: Provided file path name can not accessible by read mode

    Returns:
        list -- A list of lines of Pac-Man Map
    """
    if not isinstance(file_pathname, str):
        raise TypeError("Your file path must be a string")
    try:
        # Open the file back and read the contents
        with open(file_pathname, "r") as map_file:
            contents = map_file.read().splitlines()
    # Check if the file or directory at `path` can be found
    except FileNotFoundError:
        raise FileNotFoundError("File does not exist")
    # Check if the file or directory at `path` can be accessed by the program
    except IOError:
        raise IOError("File is not accessible")
    # Returns a list of line
    return contents


def main():
    """Demonstrate and run test"""
    file_pathname = './map/level1.amap'

    # Test wp01
    pacman_map = load_map(file_pathname)
    for line in pacman_map:
        print(line)


if __name__ == "__main__":
    main()
