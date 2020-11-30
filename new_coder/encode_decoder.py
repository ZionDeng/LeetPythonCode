cmd1 = 'abcdefg'
cmd2 = 'BCDS23g'
res = ''
# encode
for i, ch in enumerate(cmd1):
    if ch.isdigit():
        if ch == '9':
            res += '0'
        else:
            res += str((int(ch)+1))
    elif ch.isalpha():
        if ch == 'z':
            res += 'A'
        elif ch == 'Z':
            res += 'a'
        elif ch.islower():
            res += chr(ord(ch.upper())+1)
        elif ch.isupper():
            res += chr(ord(ch.lower())+1)
        
    else:
        print("something got wrong")
print(res)


# decode
res = ''
for i, ch in enumerate(cmd2):
    if ch.isdigit():
        if ch == '0':
            res += '9'
        else:
            res += str((int(ch)-1))
    elif ch.isalpha():
        if ch == 'a':
            res += 'Z'
        elif ch == 'A':
            res += 'z'
        elif ch.islower():
            res += chr(ord(ch.upper())-1)
        elif ch.isupper():
            res += chr(ord(ch.lower())-1)
        
    else:
        print("something got wrong")
print(res)
