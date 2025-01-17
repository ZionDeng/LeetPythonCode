# 合唱队

def left_max(lst):
    # 计算每个人左边出现的最多的人数
    # 186 186 150 200 160 130 197 200
    dp = [1] * len(lst)  # 若左边没有比自己小的数，则为自己本身，所以初始值为1
    for i in range(len(lst)):  # 从左往右遍历
        for j in range(i):
            if lst[j] < lst[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
        # if l[j]<l[i]:
        #     dp[i] = max(dp[i],dp[j]+1) 会超时
    return dp  # 1 1 1 2 2 1 3 4

    # 从右往左推每个人右边可以站的最多的人数
    # 3 3 2 3 2 1 1 1


while True:
    try:
        N = int(input())
        ss = list(map(int, input().split()))
        left_s = left_max(ss)
        right_s = left_max(ss[::-1])[::-1]
        sum_s = []
        for i in range(len(left_s)):
            # left_s[i]+right_s[i]-1表示此人是中间位置的人时，合唱队的人数
            sum_s.append(left_s[i] + right_s[i] - 1)
        print(str(N - max(sum_s)))
    except:
        break
