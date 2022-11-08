n=int(input())
y=abs(n)
x=str(y)
c=int(x[::-1])
#c=int(x)
if n<0:
    print(-c)
else:
    print(c)