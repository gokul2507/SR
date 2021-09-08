def isvalid(x,y):
    for i,j in zip(x,y):
        if i!='_' and j!='_':
            if i!=j:
                return 0
    return 1
def check(x,l,k):
    t=x[:k]
    for i in range(k,l-k+1,k):
        p=x[i:i+k]
        if not isvalid(t,p):
            return 0
        t=p
    if l%k:
        return (t,x[i+k:])
    return 1
x=input().strip()
l=len(x)
for i in range(1,len(x)//2+1):
    if check(x,l,i):
        q=x[:i]
        r="_" in q
        for j in range(i,l-i+1,i):
            t=x[j:j+i]
            if "_" in t or r:
                for w,e in zip(q,t):
                    if w=='_':
                        print(e)
                        exit()
                    if e=='_':
                        print(w)
                        exit()
        if l%i:
            t=x[j+i:]
            if "_" in t or r:
                for w,e in zip(q,t):
                    if w=='_':
                        print(e)
                        exit()
                    if e=='_':
                        print(w)
                        exit()
                
        break