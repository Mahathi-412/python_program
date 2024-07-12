n=int(input())
count=0
for i in range(2,n+1):
    if(n%i==0):
        count=count+1
if(count==2):
    print("The number is prime number")
else:
    print("The number is not a prime number")
