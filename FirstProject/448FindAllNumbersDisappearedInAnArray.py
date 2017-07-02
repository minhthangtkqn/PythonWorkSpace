def find_numbers(numbers):
    disappeared_number = []
    for i in xrange(len(numbers)):
        disappeared_number.extend([i + 1])
    for i in xrange(len(numbers)):
        if numbers[i] in disappeared_number:
            disappeared_number.remove(numbers[i])
    print disappeared_number
    return


if __name__ == '__main__':
    array = [4, 8, 5, 9, 4, 8, 2, 4, 6, 5]
    find_numbers(array)
