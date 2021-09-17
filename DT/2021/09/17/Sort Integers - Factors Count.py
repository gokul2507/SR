def fact(x):
    c=0
    for i in range(1,x+1):
        if x%i==0:
            c+=1
    return c
n=int(input())
l=sorted(map(int,input().split()),reverse=1)
z=[[i,fact(i)] for i in l]
z=sorted(z,key=lambda i:i[1],reverse=1)
m=sorted(set([i[1] for i in z]),reverse=1)
for i in m:
    for j in z:
        if i==j[1]:
            print(j[0],end=' ')
    print()