# 进制转换
num = input()[2:]
diction = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    '1': 1,    '6': 6,
    '2': 2,    '7': 7,
    '3': 3,    '8': 8,
    '4': 4,    '9': 9,
    '5': 5,    '0': 0,
}
result = 0
for i, digit in enumerate(num[::-1]):
    result += diction[digit] * 16 ** i
print(result)
