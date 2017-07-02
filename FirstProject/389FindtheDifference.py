import random


def find_the_difference(string, new_string):
    for i in xrange(len(string)):
        if string[i] != new_string[i]:
            print new_string[i]
            return
    print new_string[len(new_string) - 1]
    return


if __name__ == '__main__':
    prototype = 'agdtsdafs'

    #create new string by inserting a letter at random position
    insert_index = random.randint(0, len(prototype) - 1)
    new_prototype = prototype[0:insert_index] + 'J' + prototype[insert_index:len(prototype)]
    print prototype
    print new_prototype
    find_the_difference(prototype, new_prototype)
