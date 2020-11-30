while True:
    try:
        cmd = input()
        x = int(cmd)
        lst = [(n+1) * (n+2) //2 for n in range(x)]
        for i in range(x):
            print(' '.join(str(n) for n in lst))
            lst = [n - 1 for n in lst[1:]]
            
    except:
        break