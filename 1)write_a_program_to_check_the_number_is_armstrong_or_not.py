n=int(input())
sum=10
a=n
while(n!=0):
    rem=n%10
    sum=sum+rem*rem*rem
    n=n//10
if(a==sum):
    print("it is a armstrong")
else:
    print("it is not a armstrong")
