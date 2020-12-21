def maxAddSub(a, start, end):
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

if __name__ == '__main__':
    a = [1,-2,3,10,-4,7,2,-5]

    print(maxAddSub(a,0,len(a)-1))
    
    # 3 10 -4 7 2 
    # but I failed in print the list 