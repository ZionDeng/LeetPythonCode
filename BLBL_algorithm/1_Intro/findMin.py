# 旋转数组

# high and low 指针 
def findMin(num,size):
    low, high = 0, size-1
    while low < high:
        mid = (high + low) // 2 
        if num[mid] < num[high]:
            # min in the left:
            high = mid 
        elif num[mid] > num[high]:
            low = mid + 1
    return num[low]


if __name__ == '__main__':
    print(findMin([4,5,6,7,0,1,2],7))
    