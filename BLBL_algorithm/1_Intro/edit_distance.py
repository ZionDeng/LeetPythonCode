import numpy as np 

def edit_distance(s_source,s_target):
    m, n = len(s_source), len(s_target)
    dp = np.zeros((m,n))
    for i in range(m):
        dp[i,0] = i 
    for j in range(n):
        dp[0,j] = j 
    for i in range(m):
        for j in range(n):
            if s_source[i-1] == s_target[j-1]:
                dp[i,j] = dp[i-1,j-1]
            else:
                dp[i,j] = 1+ min(dp[i-1,j], dp[i-1,j-1], dp[i,j-1])
    print(dp)

edit_distance('among', 'abandon')