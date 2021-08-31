n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    if l[i]<0:
        print(l[i]*l[l[i]],end=' ')
    else:
        print(l[i]*l[l[i]-1],end=' ')