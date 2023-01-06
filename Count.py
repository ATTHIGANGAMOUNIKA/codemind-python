n=int(input())
d=list(map(int,input().split()))
c=0
o=0
for i in range(n):
    if d[i]%2==0:
        c+=1
    else:
        o+=1
print(c,o)