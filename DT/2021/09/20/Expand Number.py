s=input().strip()
l=[]
for i in range(len(s)):
    x=int(s[i])*pow(10,len(s[i:])-1)
    if x:
        l.append(str(x))
print('+'.join(l))