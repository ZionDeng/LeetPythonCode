def choose_follow(alist):
    for i in range(len(alist) - 1):
        for j in range(i, len(alist)):
            if alist[i] < alist[j]:
                alist[i], alist[j] = alist[j], alist[i]


if __name__ == '__main__':
    alist = [3, 2, 34, 2134, 213]
    choose_follow(alist)
    print(alist)
