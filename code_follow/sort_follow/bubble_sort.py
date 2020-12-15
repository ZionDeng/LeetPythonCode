
def bubble_sort(alist):
    """冒泡排序"""
    for i in range(len(alist) - 1):
        # 班长走多少趟
        count = 0
        for j in range(len(alist) - i - 1):
            # 班长从头走到尾
            if alist[j] < alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                count += 1
        if count == 0:
            # 如果班长走一趟发现没有交换，说明已经有序
            break

    print(alist)


if __name__ == '__main__':
    bubble_sort([3, 2, 33, 234, 212, 32])
