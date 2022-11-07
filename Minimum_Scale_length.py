n=int(input())
d=list(map(int,input().split()))
c=min(d)
l=0
k=0
f=[]
for i in range(1,c+1):
    if c%i==0:
        f.append(i)
for i in f:
    k=0
    for j in d:
        if j%i==0:
            k+=1
    if k==n:
        l=i
print(l)
