n= int(input())
poiList=[]
for i in range(n):
    poiList.append(list(map(int,input().split(" "))))

for point in poiList:
    valid= True
    for every in poiList:
        if point[0]<every[0] and point[1]< every[1]:
            valid= False
    if valid:
        print(point[0],point[1])