# 取整

a,b = input().split('.')
print(int(a) if int(b) < 5 else (int(a) + 1))