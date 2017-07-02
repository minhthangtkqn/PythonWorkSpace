def sum_integers(a, b):
    while (b != 0):
        carry = a & b
        a = a ^ b
        b = carry << 1
    print a
    return


if __name__ == '__main__':
    x = 19
    y = 7
    sum_integers(x, y)
