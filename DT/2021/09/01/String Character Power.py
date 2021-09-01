d={}
c=0
p={}
z=input().strip()
t=int(input())
for i in z:
    if i in d:
        if p[i]==t:
            continue
        p[i]+=1
        
        d[i]=d[i]*2
        c+=d[i]
    else:
        d[i]=1
        c+=1
        p[i]=1
print(c)