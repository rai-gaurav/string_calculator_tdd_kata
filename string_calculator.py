""" Module performing the string calculations """


def add(numbers):
    """Function adding string of numbers"""
    if not numbers:
        return 0
    numbers = map(int, numbers.split(","))
    return sum(numbers)


if __name__ == "__main__":
    print(add(""))
    print(add("1"))
    print(add("1,5"))
