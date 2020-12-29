# 线性复杂度的字符串匹配方法

# 暴力法:
# while i < len(s) and j < len(target):
#     if s[i+j] == target[0]:
#         j += 1 
#     else:
#         i += 1 
#         j = 0  # 这里的回溯导致复杂度增加

# KMP:发现不一样则移动模式串

g_s = 'abaabaabcaba'
g_pattern = 'abaabcaba'

# g_next here:
nLen = len(g_pattern)
g_next = [-1] + [0] * (nLen -1 )
# g_next = [-1] * nLen

j = 0 
k = -1 
while j < nLen -1 :
    if k == -1 or g_pattern[j] == g_pattern[k]: 
        k += 1 
        j += 1 
        g_next[j] = k
    else: 
        k = g_next[k]
print(g_next)
        
n = len(g_s)
ans = -1 
i,j = 0, 0
pattern_len = len(g_pattern)
while i < n:
    if j == -1 or g_s[i] == g_pattern[j]:
        i += 1 
        j += 1 
    else:
        j = g_next[j]
    if j == pattern_len:
        ans = i - pattern_len
        break
print(ans)
