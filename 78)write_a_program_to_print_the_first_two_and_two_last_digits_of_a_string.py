def string(s):
    if len(s)<2:
        return "empty string"
    else:
        return s[0:2]+s[-2:]
s=input()
print(string(s))
