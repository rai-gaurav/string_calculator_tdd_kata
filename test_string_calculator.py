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
    assert add("0,1,2,3,6,8,13") == 33


def test_add_leading_trailing_spaces():
    """Function should handles numbers with spaces correctly"""
    assert add(" 1 , 3 , 8 ") == 12


def test_add_large_numbers():
    """Function should handles large numbers"""
    assert add("2030080,5104073") == 7134153


def test_add_newline_characters():
    """Function should handles newline delimiter instead of comma"""
    assert add("1\n2,3") == 6


def test_add_newline_only():
    """Function should handles only newline delimiter instead of comma"""
    assert add("3\n4\n7") == 14


def test_add_mixed_delimiters():
    """Function should handles mix of multiple newline delimiter and comma"""
    assert add("2\n5,\n6\n8,11") == 32


def test_add_empty_number_between_commas():
    """Function should handles consecutive commas without number in between"""
    assert add("2,,5") == 7


def test_add_custom_delimiter():
    """Function should handles custom delimiter instead of comma"""
    assert add("//;\n1;2") == 3
    assert add("//&\n3&4&5") == 12
    assert add("//@\n4@7\n@6@21") == 38


def test_add_invalid_input():
    """Function should raise value error on invalid input"""
    with pytest.raises(ValueError):
        add("3,x")


def test_add_special_characters():
    """Function should raise value error  special character"""
    with pytest.raises(ValueError):
        add("5,9,$")


if __name__ == "__main__":
    pytest.main()
