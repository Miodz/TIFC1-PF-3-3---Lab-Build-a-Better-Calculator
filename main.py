def addmultiplenumbers(numbers):
    return sum(numbers)


def multiplymultiplenumbers(numbers):
    if not numbers:
        return 0
    result = 1
    for n in numbers:
        result *= n
    return result


def isiteven(num):
    if isinstance(num, int) and num % 2 == 0:
        return True
    return False


def isitaninteger(num):
    return isinstance(num, int)


def main():
    print("Hello learners!")


if __name__ == "__main__":
    main()