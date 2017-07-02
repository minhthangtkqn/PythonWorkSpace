def max_consecutive_ones(binary):
    # convert to integer to check value
    if int(str(''.join(map(str, binary))), 2) > 10000:
        print 'this value is too large'
        return
    else:
        print int(str(''.join(map(str, binary))), 2), ' <  10000'
        longest_ones = 0
        temp = 0
        for num in binary:
            if num == 1:
                temp = temp + 1
                longest_ones = max(temp, longest_ones)
            else:
                temp = 0
        print longest_ones
    return


if __name__ == '__main__':
    binary_array = [1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0]
    max_consecutive_ones(binary_array)
