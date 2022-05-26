n=int(input())
d=list(map(int,input().split()))
k=int(input())
sum=0
for i in range(0,n):
    if d[i]==k:
        sum=sum+d[i]
        break
    else:
        sum=sum+d[i]
print(sum)