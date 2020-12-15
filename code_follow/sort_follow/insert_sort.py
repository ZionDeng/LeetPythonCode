def insert_sort(alist):
    """插入排序"""
    # new_list = []
    # for i in range(len(alist)):
    #     count = 0
    #     for j in range(len(new_list)):
    #         if alist[i] <= new_list[j]:
    #             new_list.insert(j, alist[i])
    #             count += 1
    #     if count == 0:
    #         new_list.append(alist[i])
    # return new_list

    for i in range(len(alist)):
        for j in range(i):
            if alist[i] < alist[j]:
                alist[i], alist[j] = alist[j], alist[i]


if __name__ == '__main__':
    alist = [3, 2, 23, 231, 43]
    insert_sort(alist)
    print(alist)
