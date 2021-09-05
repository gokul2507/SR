s=input().strip()
l,t=[],''
for i in range(len(s)-1):
    if s[i+1]!=s[i]:
        t+=s[i]
        l.append(int(t))
        t='' 
    else:
        t+=s[i] 
l.append(int(t+s[-1]))
print(sum(l))