def keyboard_row(list):
    row = []
    row.append(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
    row.append(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'])
    row.append(['z', 'x', 'c', 'v', 'b', 'n', 'm'])

    # xet theo tung` hang` ban` phim'
    for row_index in xrange(len(row)):

        # xet theo tu`ng tu`
        for word in xrange(len(list)):
            print '--------------'
            print 'row: ', row_index
            print 'word: ', word
            if check_if_exist(row[row_index], list[word]) == 'true':
                print list[word]

    return 'DONE'


def check_if_exist(row, word):
    check = ''

    for letter in xrange(len(word)):
        check = 'false'
        for row_letter in xrange(len(row)):
            if word[letter] == row[row_letter]:
                check = 'true'
                break
        if check == 'true':
            pass
        else:
            return check

    return check


if __name__ == '__main__':
    words_list = ['assasas', 'hyphen', 'dad', 'khadas', 'qiwuqwrowq', 'alaska']
    keyboard_row(words_list)