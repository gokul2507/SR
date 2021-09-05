n,s=int(input()),0
l=list(map(int,input().split()))
if n%2: print(-1); exit()
for i in range(0,n,2):
    s+=l[i+1]-l[i] 
print(s)