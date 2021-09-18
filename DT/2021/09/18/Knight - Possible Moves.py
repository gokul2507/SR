m=[list(map(str,input().split())) for i in range(8)]
def check(x,y):
    f=0
    if 0<=x+2<8 and 0<=y+1<8: f+=1 
    if 0<=x+2<8 and 0<=y-1<8: f+=1 
    if 0<=x-2<8 and 0<=y+1<8: f+=1 
    if 0<=x-2<8 and 0<=y-1<8: f+=1 
    if 0<=x+1<8 and 0<=y+2<8: f+=1 
    if 0<=x-1<8 and 0<=y+2<8: f+=1 
    if 0<=x+1<8 and 0<=y-2<8: f+=1 
    if 0<=x-1<8 and 0<=y-2<8: f+=1 
    return f
for i in range(8):
    for j in range(8):
        if m[i][j]=='H':
            c=check(i,j)
            break
print(c)