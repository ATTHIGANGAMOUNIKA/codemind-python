n=(input())
t=n.split()
c=[]
for i in range(len(t)):
    v=len(t[i])
    c.append(v)
for j in range(len(c)):
    mx=c[0]
    if mx>c[i]:
        mx=c[j]
print(mx)