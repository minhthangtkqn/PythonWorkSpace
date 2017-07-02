# chon ra banh' quy nao nho? nhat co the cho moi dua' con
def assign_cookies(children, cookies):

    count = 0
    for i in xrange(len(children)):
        # assume you give this child the largest cookie
        temp = max(cookies)
        # check if your child is content or not (default: not)
        is_assigned = 0

        for j in xrange(len(cookies)):
            if children[i] <= cookies[j] and cookies[j] <= temp:
                temp = cookies[j]
                is_assigned = 1
        if is_assigned == 1:
            cookies.remove(temp)
            count += 1

    print count
    return 0

if __name__ == '__main__':
    children_list = [1,3,4,5,7,8]
    cookies_list = [2,2,3,6,6]
    assign_cookies(children_list, cookies_list)