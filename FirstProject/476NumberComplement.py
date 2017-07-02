def number_complement(number):
    # check number's value
    if number >= pow(2, 32) or number <= 0:
        return 'DU LIEU BAN NHAP PHAI NAM TRONG KHOANG  0 < VALUE < 2^32'

    count = 32

    # starting find number complement
    while count > 0:
        if number < pow(2, count - 1):
            print number, ' < ', pow(2, count - 1)
            count -= 1
        else:
            break

    destination_number = pow(2, count) - 1 - number
    print 'COMPLEMENT NUMBER OF ', number, ' IS ', destination_number
    print bin(number)
    print bin(destination_number)
    return 'DONE'

if __name__ == '__main__':
    a = 155
    print number_complement(a)