x,y=map(int,input().split())
if x>y:
    print("0 "*y)
    exit()
l=[0 for _ in range(1,x)]
l.append(1)
print(*l,end=' ')
y-=x
t=sum(l)
while y>0:
    y-=1
    print(t,end=' ')
    l.append(t)
    t-=l.pop(0)-t