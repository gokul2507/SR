s=input().strip()
c=0 
for i in range(1,10):
    n=str(i)*2+str(i+1)*2 
    for j in s:
        if n and n[0]==j:
            n=n[1:]
    if not n:
        c+=1 
print(c)