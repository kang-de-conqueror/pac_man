#!/usr/bin/env python3
import pytest

from game import load_map

def test_load_map():
    file_path = "./map/level1.amap"
    assert isinstance(load_map(file_path), list)

    error_file_path = "./map/level1.amappp"
    with pytest.raises(FileNotFoundError):
        load_map(error_file_path)

    int_file_path = 123
    with pytest.raises(TypeError):
        load_map(int_file_path)

