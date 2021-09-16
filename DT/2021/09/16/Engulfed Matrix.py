r,c=map(int,input().split())
z=[list(map(int,input().split())) for i in range(r)]
m,n=map(int,input().split())
p,q=map(int,input().split())
for i in range(min(m,n),max(m,n)-1):
    for j in range(min(p,q),max(p,q)-1):
        print(z[i][j],end=' ')
    print()