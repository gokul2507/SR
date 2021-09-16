n=int(input())
prev=0
for i in range(1,n+1):
    if i%2:
        print(*[j for j in range(prev,i*i+1) if j%2])
    else:
        print(*[j for j in range(prev,i*i+1) if j%2==0])
    prev=i*i