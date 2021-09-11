d={}
s=input().strip()
x,t=s[0],''
for i in range(1,len(s)):
    if s[i].isdigit():
        t+=s[i]
    elif s[i].isalpha():
        d[x]=d.get(x,0)+int(t)
        t=''
        x=s[i]
d[x]=d.get(x,0)+int(t)
for i in sorted(d.items()):
    print(i[0],i[1],sep='',end='')