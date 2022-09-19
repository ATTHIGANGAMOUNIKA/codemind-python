n=int(input())
d=list(map(int,input().split()))
for i in range(n):
    if d[i]%2!=0:
        print(False)
        break
else:
    print(True)
