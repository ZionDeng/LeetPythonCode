# list have 0,1,2
# change to 000,,,111,,,222,,,
# 3 cursor: begin, current, end 

def Holland(a):
    begin, cur, end = 0,0,len(a) -1 
    while cur <= end:
        if a[cur] == 2:
            a[end], a[cur] = a[cur], a[end]
            end -= 1 
        elif a[cur] == 1:
            cur += 1 
        else:  # a[cur] == 0
            # if begin == cur:
            #     begin += 1 
            #     cur += 1 
            # else: 
            #     a[cur], a[begin ] = a[begin], a[cur]
            #     begin += 1 
            a[cur], a[begin ] = a[begin], a[cur]
            begin += 1 
            cur += 1 


    print(a)


Holland([0,2,1,2,0,1,1,2])
