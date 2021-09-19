n=int(input())
l=list(map(int,input().split()))
k=int(input())
for i in l[:k]:
    for j in range(k,n):
        l[j]+=l[j]%i 
print(*l)