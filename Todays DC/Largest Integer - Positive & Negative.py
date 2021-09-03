n=int(input())
l=list(map(int,input().split()))
z=[i for i in l if i*-1 in l]
print(max(z)) if z else print(-1)