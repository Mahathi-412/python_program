s=input()
a=s.split()
result=""
for i in a:
    result=result+i[0].upper()+i[1:-1]+i[-1].upper()
print(result)
