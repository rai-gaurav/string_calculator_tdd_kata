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
    assert add("2030080,5104073") == 0
    assert add("2,1001") == 2
    assert add("1000,1001") == 1000


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


def test_add_custom_delimiter_with_newlines():
    """Function should handles custom delimiter with newlines"""
    assert add("//@\n4@7\n@6@21") == 38


def test_add_negative_numbers():
    """Function should raise exception in case of negative number"""
    with pytest.raises(ValueError, match="negative numbers not allowed -4"):
        add("13,-4,8")


def test_add_multiple_negative_numbers():
    """Function should raise exception and exception message, separated by commas in case of multiple negative numbers"""
    with pytest.raises(ValueError, match="negative numbers not allowed -3,-34"):
        add("12,-3,-34,67")


def test_add_custom_delimiter_with_negative_numbers():
    """Function should handles custom delimiter with negative numbers"""
    with pytest.raises(ValueError, match="negative numbers not allowed -6,-7"):
        add("//@\n-6@3@-7")


def test_add_invalid_input():
    """Function should raise value error on invalid input"""
    with pytest.raises(ValueError):
        add("3,x")


def test_add_special_characters():
    """Function should raise value error special character"""
    with pytest.raises(ValueError):
        add("5,9,$")


def test_add_custom_delimiter_any_length():
    """Function should be able to handles custom delimiter of any length"""
    assert add("//[***]\n1***2***3") == 6
    assert add("//[$$]\n3$$6$$8") == 17
    assert add("//[^Z]\n32^Z643^Z845") == 1520  # Control Character
    assert (
        add("//[éï«ù╬Ä]\n2éï«ù╬Ä\n453éï«ù╬Ä62") == 517
    )  # French language characters as delimiter


if __name__ == "__main__":
    pytest.main()
