def ransom_note(ransom, magazine):
    amount = [0] * 26
    # counting amount of each letter in magazine
    for i in xrange(len(magazine)):
        amount[ord(magazine[i]) - ord('a')] += 1

    # check if lack of letters
    for i in xrange(len(ransom)):
        if amount[ord(ransom[i]) - ord('a')].__sub__(1) < 0:
            print 'false'
            return

    print 'true'
    return


if __name__ == '__main__':
    ransom = 'absb'
    magazine = 'aaabbssss'
    ransom_note(ransom, magazine)
