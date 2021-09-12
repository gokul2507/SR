m=[list(map(str,input().strip())) for i in range(4)]
for i in zip(*m):
    x=''.join(i)
    if '0' in x or '1' in x:
        print(int(x,2),end='')
    else:
        print(':',end='')