# 输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
nums = list(input())
nums_order = list(set(nums))
nums_order.sort()
for i in nums_order: 
    print(i, end="")
