s=input().strip()
c,x,y=1,0,0 
l=[]
for i in range(1,len(s)):
    if c==0:
        y=i
        l.append(s[x:y])
        x=y
    if s[i]=='(':
        c+=1 
    else:
        c-=1
l.append(s[x:])
print(*l,sep='\n')