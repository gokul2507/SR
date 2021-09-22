a,b,c=map(int,input().split())
print(*sorted([a,b,c,a+b,b+c,c+a,a+b+c]))