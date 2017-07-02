def reserve_string(string):
    new_string = list(string)

    for i in xrange(len(string)):
        new_string[i] = string[len(string) - 1 - i]

    new_string = ''.join(new_string)
    print 'RESERVE STRING: ', new_string
    return 0


if __name__ == '__main__':
    input_string = 'hoang minh thang'
    reserve_string(input_string)
