# 1234 -> 4! = 24 
# 全排列

def permutation(string, begin, end): 
    s = list(string)
    if begin == end:
        print(''.join(s), end = ' ')
        return
    for i in range(begin,end+1,1):
        if s[i] in s[begin: i]:
            # 判断是否重复，如果重复就不能放在第一位，
            # 所以就不行
            continue
        s[i], s[begin] = s[begin], s[i] # 把s[i]放在第一位
        permutation(s,begin+1, end)
        s[i], s[begin] =  s[begin], s[i] # 把顺序弄回来
        

permutation('1223',0, 3)

# 非递归算法：按字典顺序
# 后找,小大,交换,翻转
# 21543 -> 23145

# def next_permutation(string):
#     s = list(string)
#     end = len(string) 
#     start = 0 
#     while end > 0:
#         q = end 
#         end -= 0 
#         if s[end] < s[start]:
#             p_find = p_end 
#             while s[p_find] <= s[end]
