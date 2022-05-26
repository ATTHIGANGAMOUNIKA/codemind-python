n=int(input())
d=list(map(int,input().split()))
sum=0
for i in d:
    if i%2!=0:
        sum=sum+i
    if i%2==0:
        break

print(sum)