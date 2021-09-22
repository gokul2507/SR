r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
l=[]
for i in m:
    for j in i:
        if j%2: l.append(j)
l=sorted(l)
for i in range(r):
    for j in range(c):
        if m[i][j]%2:
            print(l.pop(0),end=' ')
        else:
            print(m[i][j],end=' ')
    print()