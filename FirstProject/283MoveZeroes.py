def move_zeroes(array):
    difference = 0
    for i in xrange(len(array)):
        if array[i - difference] == 0:
            array.pop(i - difference)
            array.extend([0])
            difference += 1
    print array
    return


if __name__ == '__main__':
    array_numbers = [0, 0, 0, 0, 15, 2, 0, 4, 8]
    move_zeroes(array_numbers)
