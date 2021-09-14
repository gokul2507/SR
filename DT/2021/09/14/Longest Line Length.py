d={}
for i in range(int(input())):
    a,b=map(int,input().split())
    d[b]=d.get(b,[])+[a]
abcd=lambda i:abs(sorted(i)[0]-sorted(i)[-1])
get=lambda i:abcd(d[i])
m=max(d,key=get)
t=sorted(d[m])
print(abs(t[0]-t[-1])) if len(t)>1 else print(-1)