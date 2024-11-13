a=input()
c={}
for i in a:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
print(c)
        
