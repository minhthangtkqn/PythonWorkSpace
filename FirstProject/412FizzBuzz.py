def fizz_buzz(value):
    for i in xrange(value):
        if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
            print 'FizzBuzz'
        else:
            if (i + 1) % 3 == 0:
                print 'Fizz'
            else:
                if (i + 1) % 5 == 0:
                    print 'Buzz'
                else:
                    print i + 1
    return 0


if __name__ == '__main__':
    n = 19
    fizz_buzz(n)
