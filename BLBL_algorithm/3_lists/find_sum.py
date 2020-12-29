# find 2 num in a list whose sum is sum
# 排序加两头扫


def twoSum(ls,target):
    begin = 0 
    end = len(ls)-1

    while begin < end: 
        cur = ls[begin] + ls[end] 
        if cur == target:
            print(ls[begin],ls[end])
            break
        else:
            if cur < target:
                begin += 1 
            else:
                end -= 1


twoSum([2,25,3,21,43,1],3)


def allSum(ls, target):
    '''暴力法'''
    size = len(ls)
    x = [False] * size  # the T/F set for the res 
    has = 0 
    i = 0 

    def enum_number(x, i, has):
        '''
        x: the bool set of the result 
        i: the number now is inspecting
        has: the sum now 
        '''
        if i >= size:
            return
        if has + ls[i] == target:
            x[i] = True 
            print() 
            print([j for j,t in zip(ls,x) if t ])
            x[i] = False
        x[i] = True 
        enum_number(x, i+1 , has +ls[i])
        x[i]  = False
        enum_number(x, i+1, has)
    enum_number(x, i, has)
    


ls = [1,2,3,4,5]
print('original list is: ', ls)
allSum(ls,10)

