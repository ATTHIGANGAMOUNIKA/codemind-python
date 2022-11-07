n=int(input())
d=list(map(int,input().split()))
c=min(d)
a=0
for i in range(n):
    if d[i]%c==0:
        a+=1
if a==n:
    print(c)
else:
    print("1")
        