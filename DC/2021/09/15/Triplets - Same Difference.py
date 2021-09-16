n,f=int(input()),1
l=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if len(set([l[i],l[j],l[k]]))==3 and abs(l[i]-l[j])==abs(l[j]-l[k]):print(l[i],l[j],l[k])
            f=0
if f:print(-1)