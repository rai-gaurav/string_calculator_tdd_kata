""" Test Cases for String Calculations """

import pytest
from string_calculator import add


def test_add_empty_string():
    """Function should handles empty string"""
    assert add("") == 0


def test_add_single_number():
    """Function should handles singlr integer"""
    assert add("1") == 1


def test_add_two_number():
    """Function should handles couple of integer"""
    assert add("1,5") == 6


def test_add_multiple_numbers():
    """Function should handles multiple integer"""
    assert add("1,2,3,6,8,13") == 33


def test_add_leading_trailing_spaces():
    """Function should handles numbers with spaces correctly"""
    assert add(" 1 , 3 , 8 ") == 12


def test_add_large_numbers():
    """Function should handles large numbers"""
    assert add("2030080,5104073") == 7134153


def test_add_invalid_input():
    """Function should handles invalid input"""
    with pytest.raises(ValueError):
        add("3,x")


if __name__ == "__main__":
    pytest.main()
