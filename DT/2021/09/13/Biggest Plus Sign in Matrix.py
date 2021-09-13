x,y=map(int,input().split())
z=[input().split() for _ in range(x)]
def do(q,w):
    if (not 0<=q<x) or (not 0<=w<y):
        # print("1sr")
        return 1
    if z[q][w]!='1':
        # print(z[q][w],q,w)
        # print("2nd")
        return 1 
    return 0    
def check(sr,sc,q,w):
    if do(sr+q,sc) or do(sr-q,sc) or do(sr,sc+w) or do(sr, sc-w):
        # print("end=",sr,sc,q,w)
        return 0
    # print(sr,sc)
    return check(sr,sc,q+1,w+1)+1
m=-1
for i in range(x):
    for j in range(y):
        if z[i][j]=='1':
            t=check(i,j,0,0)
            if t>1 and m<t:
                m=t
print(m)