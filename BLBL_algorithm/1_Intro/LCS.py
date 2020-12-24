# 最长公共子序列（不要求连续），子串需要连续
# acdfg adfac -> adf 
# 长度为m,n
# 暴力法： O(2**m,2**n) -> 不可取
# LCS(Xm,Yn) = LCS(Xm-1,Yn-1) + xm = W + xm
# W: Xm-1, Yn-1的最长公共子序列
# if len1, len2 == 0:
#     return ''
# if s1[-1] == s2[-1]:
#     return LCS(s1[:-1],s2[:-1]) + 1 
# else:
#     return max(LCS(s1[:-1],s2),LCS(s1,s2[:-1]))

def LCS(s1,s2):
    if len(s1) == 0 or len(s2) == 0:
        return ''
    if s1[-1] == s2[-1]:
        return LCS(s1[:-1],s2[:-1]) + s1[-1]
    else:
        return LCS(s1[:-1],s2) if len(LCS(s1[:-1],s2)) > len(LCS(s1,s2[:-1])) else LCS(s1,s2[:-1]) 

import numpy as np 

def print_lcs(s1,s2):
    ls = np.zeros((len(s1),len(s2)))
    for i in range(1,len(s1)):
        for j in range(1,len(s2)):
            if s1[i] == s2[j]:
                ls[i,j] = ls[i-1,j-1] + 1 
            elif ls[i-1,j] >= ls[i,j-1]:
                ls[i,j] = ls[i-1,j]
            else:
                ls[i,j] = ls[i,j-1]
    print(ls)




if __name__ == '__main__':
    string1 = 'ABCBDAB'
    string2 = 'BDCABA'
    print(LCS(string1,string2))
    print_lcs(string1,string2)

# application： LIS, edit_distance