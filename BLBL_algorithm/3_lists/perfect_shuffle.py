# [a1,a2,,,b1,b2,,] -> [a1,b1,a2,b2,,,]

# time: O(n), space:O(1)

# first n -> 2n 
# last n ->  (2*i) % (2*n+1) 
# -> sum up 

def cycleLeader(a,start, mod):

    i = (start * 2) % mod 
    while i is not start:
        a[i], a[start] = a[start], a[i]
        i = i * 2 % mod 

# ls = [1,2,3,4,5,6,7,8]
# cycleLeader(ls,1,5)
# print(ls)


def right_rotate(ls,start, end):
    pass 
def perfect_shuffle(a, n):
    while n > 1:
        n2 = n * 2 
        k, m = 0, 1 
        while n2 / m >= 3:
            m /= 2 
            right_rotate(a+m,m,n)
            i, t = 0, 1 
            while i < k: 
                cycleLeader(a,t, m*2 + 1)
            i += 1
            t *= 3 
        k +=1 
        m *= 3 
    a[1], a[2] = a[2], a[1]


ls = list(range(1,9,1))
perfect_shuffle(ls, 4)
print(ls)