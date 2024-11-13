def string(s1):
    n=s1[0]
    s1=s1.replace(n,"$")
    s1=n+s1[1:]
    return s1
s1=input()
print(string(s1))
        
