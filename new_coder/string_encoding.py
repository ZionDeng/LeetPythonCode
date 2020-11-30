cmd1, cmd2 = input().split()
res = cmd1 + cmd2
temp1 = [res[i] for i in range(0, len(res), 2)]
temp2 = [res[i] for i in range(1, len(res), 2)]

res2 = ''
for x, y in zip(sorted(temp1), sorted(temp2)):
    res2 = res2 + x + y
res = ''
for i in res2:
    if i.isdigit() or i in 'abcdefABCDEF':
        s = bin(int(i,16))[2:]
        res += hex(int(s[::-1],2))[-1]
    else:
        res += i
print(res.upper())