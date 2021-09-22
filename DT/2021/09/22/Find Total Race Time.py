import time
x=0
for i in range(int(input())):
    x+=int(input().strip(),2)
d=time.strftime("%H:%M:%S",time.gmtime(x))
print(d)