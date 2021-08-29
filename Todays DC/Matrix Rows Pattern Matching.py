r,c=map(int,input().split())
m=[input().split() for i in range(r)]
s=input().strip()
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]==s[j] and m[i]!=m[j]:
            print("NO")
            exit()
        elif s[i]!=s[j] and m[i]==m[j]:
            print("NO")
            exit()
print("YES")