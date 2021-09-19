n,p=map(int,input().split())
l=[1,1,1]
l[p-1]=0
for i in range(n):
    a,b=map(int,input().split())
    a,b=a-1,b-1 
    l[a],l[b]=l[b],l[a] 
print(l.index(0)+1)