""" Module performing the string calculations """


def add(numbers):
    """Function adding string of numbers"""
    if not numbers:
        return 0

    delimiter = ","  # default value
    if numbers.startswith("//"):
        # split inot two part on first \n encounter
        delimiter_section, number_section = numbers.split("\n", 1)
        # Remove the first two char from the slice (//) and delimiter will be sfter that
        delimiter = delimiter_section[2:]
        # After delimiter, second slice will contain actual numbers
        numbers = number_section

    # Replace new line with delimiter
    numbers = numbers.replace("\n", delimiter)
    # In case we have consecutive multiple delimiter without a number in between
    number_list = [num for num in numbers.split(delimiter) if num.strip()]
    # map returns an iterator, need to convert it to list
    number_list = list(map(int, number_list))

    # Check for negative number
    negative_numbers = [num for num in number_list if num < 0]
    if negative_numbers:
        raise ValueError(
            "negative numbers not allowed {}".format(
                ",".join(map(str, negative_numbers))
            )
        )

    # Ignore numbers larger than 1000
    number_list = [num for num in number_list if num <= 1000]

    return sum(number_list)


# if __name__ == "__main__":
#     print(add(""))
#     print(add("1"))
#     print(add("1,5"))
#     print(add("1\n2,3"))
#     print(add("//;\n6;2"))
#     print(add("2,1001"))
#     print(add("2, -6, -3"))
