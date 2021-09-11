a,b,p=input().strip(),input().strip(),0 
c,m=0,0
for i,j in enumerate(a):
    if j=='(': 
        c+=1 
    else: 
        c-=1
    if c>m: 
        p=i
        m=c 
print(a[:p+1]+b+a[p+1:])