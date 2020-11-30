val = input()
tmp = val.split(";")
x, y = 0, 0
comp = set("1234567890")
for i in tmp:
    if not i or i[0] not in ["A", "D", "W", "S"] or set(i[1:]).issubset(set("1234567890")) == False:
        continue
    elif i[0] == "A":
        x -= int(i[1:])
    elif i[0] == "S":
        y -= int(i[1:])
    elif i[0] == "W":
        y += int(i[1:])
    elif i[0] == "D":
        x += int(i[1:])
print(str(x)+","+str(y))
