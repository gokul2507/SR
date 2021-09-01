d={0:1,1:0,2:0,3:0,4:1,5:0,6:1,7:0,8:2,9:1}
n=int(input())
for i in range(1,n+1):
    s=0
    for j in str(i):
        s+=d.get(int(j))
    if s>=len(str(i)):
        print(i,end=' ')