def detect_capital(word):
    if len(word) == 1:
        return 'TRUE'
    else:
        if ord(word[0]) > 64 and ord(word[0]) < 91:  # 1st is Capital
            if ord(word[1]) > 64 and ord(word[1]) < 91: # second letter is Capital
                for i in xrange(2, len(word)):
                    if ord(word[i]) > 96 and ord(word[i]) < 123:
                        return 'FALSE'
            else: # second letter is not Capital
                for i in xrange(2, len(word)):
                    if ord(word[i]) > 64 and ord(word[i]) < 91:
                        return 'FALSE'
        else:  # 1st is not Capital
            for i in xrange(1, len(word)):
                if ord(word[i]) > 64 and ord(word[i]) < 91:
                    return 'FALSE'
    return 'TRUE'


if __name__ == '__main__':
    a = 'DgtdsL'
    print detect_capital(a)
