""" Module performing the string calculations """


def add(numbers):
    """Function adding string of numbers"""
    if not numbers:
        return 0

    # Replace new line delimiter with comma
    numbers = numbers.replace("\n", ",")
    # In case we have consecutive multiple commas without a number in between
    number_list = [num for num in numbers.split(",") if num.strip()]
    number_list = map(int, number_list)
    return sum(number_list)


if __name__ == "__main__":
    print(add(""))
    print(add("1"))
    print(add("1,5"))
    print(add("1\n2,3"))
