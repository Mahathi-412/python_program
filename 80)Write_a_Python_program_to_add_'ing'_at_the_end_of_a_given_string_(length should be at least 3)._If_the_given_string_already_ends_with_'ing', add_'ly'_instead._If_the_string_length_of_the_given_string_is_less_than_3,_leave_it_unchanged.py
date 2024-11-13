def string(s1):
    n=len(s1)
    if n<3:
        return s1
    elif 'ing' in s1:
        return s1+'ly'
    else:
        return s1+'ing'
s1=input()
print(string(s1))
