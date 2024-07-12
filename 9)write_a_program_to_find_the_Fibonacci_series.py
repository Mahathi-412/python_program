n=int(input())
a=0
b=1
c=a+b
print(a,b)
for i in range(1,n+1):
    print(c)
    a=b
    b=c
    c=a+b
