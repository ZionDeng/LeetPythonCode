"""二分法查找"""
def bi_search(alist,item):
    # 递归方法一定要有返回
    if len(alist)>0:
        mid = len(alist)//2
        if item < alist[mid]:
            return bi_search(alist[:mid],item)
        elif item > alist[mid]:
            return bi_search(alist[mid+1:],item)
        else:
            return mid 
    else:
        return False

def bi_search_2(alist,item):
    n= len(alist)
    first= 0
    last= n-1
    # 这儿的last应该放在外面
    while n>0 :
        mid = (first + last) //2
        if alist[mid] == item:
            return mid 
        elif item< alist[mid]:
            last= mid-1 
        else:
            first = mid+1
        n = last-first 
    return False
    


if __name__=='__main__':
    lst = [1,3,4,6,7,8,10,13,14]
    # print(bi_search(lst,4))
    print(bi_search_2(lst,4))
