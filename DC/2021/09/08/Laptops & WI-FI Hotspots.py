s=list(input().strip())
n=len(s)
for i in range(n):
    c=0 
    if s[i]=='L':
        a,b=s[:i][::-1],s[i+1:] 
        if '#' in a:
            c+=a[:a.index('#')].count('*')
        else:
            c+=a.count('*') 
        if '#' in b:
            c+=b[:b.index('#')].count('*')
        else:
            c+=b.count('*') 
        print(c,end=' ')