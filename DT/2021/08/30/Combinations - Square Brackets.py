s=list(input().strip())
p=s.index('[')
z,z2=s[:s.index('[')],s[s.index(']')+1:]
l=s[s.index('[')+1:s.index(']')]
l=''.join(l).split("|")
for i in sorted(l):
    print(''.join(z)+i+''.join(z2),end=' ')