n=int(input())
c=1
for i in range(n-1):
    print("*"*i,c,sep='')
    c+=1
print(*range(c,c+n)[::-1],sep='')
c+=n
for i in range(1,n):
    print("*"*i,c,sep='');
    c+=1