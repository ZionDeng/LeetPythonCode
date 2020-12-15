def shell_sort(alist):
    """希尔排序"""

    n = len(alist)
    gap = n // 2
    while gap >= 1:
        for j in range(gap, n):
            i = j
            while i >= gap:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2


if __name__ == '__main__':
    alist = [3, 2, 23, 434, 32,432,21,342]
    shell_sort(alist)
    print(alist)
