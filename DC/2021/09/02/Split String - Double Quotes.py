l=input().split()
f=0 
for i in l:
    if i[0]=="\"":
        f=1 
    if i[-1]=="\"":
        f=0 
    if f:
        print(i.replace("\"",""),end=' ')
    else:
        print(i.replace("\"",""))