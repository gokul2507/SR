l=input().split()
z=[]
f=1
for i in l:
    if i[0]=='[':
        f=0
    if f:
        z.append(int(i)) 
    if i[-1]==']':
        f=1
z=sorted(z)
f=1
for i in l:
    if i[0]=='[':
        f=0 
    if f:
        print(z.pop(0),end=' ' )
    if i[-1]==']':
        f=1 
        print(i,end=' ')
    elif f==0:
        print(i,end=' ')