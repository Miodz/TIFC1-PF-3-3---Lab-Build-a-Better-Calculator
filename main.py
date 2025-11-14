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
    addmultiplenumbers([5,9])
    print(multiplymultiplenumbers([5,9.3]))
    print(isiteven([5,-7,9.3]))
    print(isitaninteger([5,-7,9.3]))


if __name__ == "__main__":
    main()