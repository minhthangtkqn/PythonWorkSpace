def hamming_distance(x, y):
    if x < 0 or x >= pow(2, 31) or y < 0 or y >= pow(2, 31):
        return 'Inputted value are wrong'

    print 'x = ', bin(x)
    print 'y = ', bin(y)
    print '-------------'
    count = 0
    while x > 0 or y > 0:
        # minimum bit of x and x
        # default 0
        bin_x = 0
        bin_y = 0

        # get minimum bit of x
        if x > 0:
            bin_x = x % 2
            x = x / 2

        # get minimum bit of y
        if y > 0:
            bin_y = y % 2
            y = y / 2

        # compare minimum bits
        if bin_x != bin_y:
            count += 1
    # show how many bits are different
    print 'HAMMING NUMBER = ', count
    return 'DONE'


if __name__ == '__main__':
    a = 132
    b = 144

    print hamming_distance(a, b)
