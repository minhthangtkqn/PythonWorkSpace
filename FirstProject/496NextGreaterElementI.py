def next_greater_element(child_list, root_list):
    # create greater array
    greater = child_list[:]
    for i in xrange(len(greater)):
        greater[i] = -1

    for i in xrange(len(child_list)):

        for j in xrange(root_list.index(child_list[i]), len(root_list)):
            if root_list[j] > child_list[i]:
                greater[i] += 1
        if greater[i] >= 0:
            greater[i] = greater[i] + 1

    print greater
    return 0


if __name__ == '__main__':
    child = [2, 4]
    root = [1, 2, 3, 4]
    next_greater_element(child, root)
