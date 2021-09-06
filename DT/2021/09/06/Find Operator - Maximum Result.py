a,b=map(int,input().split())
p=['*','-','+','/']
z=[a*b,a-b,a+b,a//b]
print(p[z.index(max(z))])