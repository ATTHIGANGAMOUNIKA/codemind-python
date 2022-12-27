n=int(input())
d=list(map(int,input().split()))
c=sum(d)
if c%2==0:
    print("1")
else:
    print("0")