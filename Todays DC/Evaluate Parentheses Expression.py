a,b,c=0,0,'' 
for i in input().strip():
    if i=='(':
        if c: b+=(int(c)*a)
        a+=1 ;c=''
    elif i==')':
        if c: b+=(int(c)*a)
        a-=1;c=''
    else: c+=i
print(b)