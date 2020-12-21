def maxAddSub(a, start, end):
    '''
    idea: divide it to 3 parts: left/ right/ both
    '''
    if end == start:
        return a[start]

    middle = (start + end) // 2 
    m1 = maxAddSub(a, start,middle)
    m2 = maxAddSub(a,middle+1, end)

    left,right = a[middle], a[middle+1]
    now = a[middle]
    for i in range(middle -1, start -1, -1):
        now += a[i]
        left = max(now,left)
        # left = now if sum(now) >= sum(left) else left
        
    now = a[middle +1]
    for i in range(middle+2, end+1,1):
        now += a[i]
        right = max(now,right)
        # right = now if sum(now) >= sum(right) else right
    m3 = left + right 
    return max(m1,m2,m3)


def maxAddSub_dyn(a):
    res = a[0]
    sum_a = a[0]
    for i in range(1,len(a) -1,1):
        # if sum_a > 0:
        #     sum_a += a[i]
        # else:
        #     sum_a = a[i]
        # if sum_a  > res: 
        #     res = sum_a 

        sum_a = sum_a + a[i] if sum_a > 0 else a[i]
        res = max(res,sum_a)
    return res 

def maxAddSub_lst(a):
    res = [a[0]]
    it = [a[0]]
    for i in range(1,len(a)-1,1):
        it = it + [a[i]] if sum(it) > 0 else [a[i]]
        res = max(it,res)
    return res 


if __name__ == '__main__':
    a = [1,-2,3,10,-4,7,2,-5]

    print(maxAddSub(a,0,len(a)-1))
    
    # 3 10 -4 7 2 
    # but I failed in print the list 

    print(maxAddSub_dyn(a))
    print(maxAddSub_lst(a))