def string(s):
    a=s.find("not")
    b=s.find("poor")
    if a!=-1 and b!=-1 and a<b:
        s=s[:a]+'good'+s[b+4:]
        return s
    else:
        return s
s=input()
print(string(s))
