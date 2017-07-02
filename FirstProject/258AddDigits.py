def add_digits(number):
    if number < 10:
        return number
    else:
        sum_digits = 0
        while number > 0:
            sum_digits = sum_digits + (number % 10)
            number = number / 10
        return add_digits(sum_digits)


if __name__ == '__main__':
    x = 3868
    print add_digits(x)
