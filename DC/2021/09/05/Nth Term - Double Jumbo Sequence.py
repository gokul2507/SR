n=int(input())
l=[0,1]
for i in range(n-2):
    l.append(l[-1]+(2*l[-2]+3))
print(l[n-1])