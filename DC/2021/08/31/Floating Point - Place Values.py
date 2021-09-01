z=input().split('.')
a,b=list(z[0]),list(z[1])
for i in range(len(a)):   
    p=len(a)-i-1
    print(int(a[i])*pow(10,p),end=' ')
for i in range(len(b)):   
    print("%d/%d"%(int(b[i]),pow(10,i+1)),end=' ') if b[i]!='0' else print(0,end=' ')