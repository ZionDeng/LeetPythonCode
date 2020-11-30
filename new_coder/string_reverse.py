while True:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        nums.sort()
        flag = int(input())
        if flag == 0:
            print(' '.join(str(i) for i in nums))
        if flag == 1:
            print(' '.join(str(i) for i in nums[::-1]))

    except:
        break
