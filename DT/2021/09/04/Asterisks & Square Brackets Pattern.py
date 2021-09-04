n=int(input())
h,b,s=n*2-2,1,1
for i in range(n):
    print('-'*h,'['*b,'*'*s,']'*b,'-'*h,sep='')
    h-=2
    s+=2 
    b+=1 