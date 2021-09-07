r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
count=0 
for i in range(r):
    for j in range(c):
        if m[i][j]==int(str(i+1)+str(j+1)):
            count+=1 
print(count)