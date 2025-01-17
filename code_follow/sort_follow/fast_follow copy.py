def quick_sort(alist, start, end):
    """快速排序"""
    if start > end:
        return 
    mid = alist[start]
    low, high = start, end 

    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1 
        alist[low] = alist[high]

        while low < high and alist[low] < mid:
            low += 1 
        alist[high] = alist[low]
        
    
    alist[low] = mid 

    quick_sort(alist,start,low-1)

    quick_sort(alist,low+1,end)



if __name__ == '__main__':
    lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(lst, 0, len(lst)-1)
    print(lst)
