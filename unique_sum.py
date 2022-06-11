n=int(input())
d=list(map(int,input().split()))
b=[]
for i in d:
    if i not in b:
        b.append(i)
b=sum(b)
print(b)
