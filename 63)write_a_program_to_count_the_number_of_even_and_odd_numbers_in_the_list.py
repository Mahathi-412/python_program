arr=[1,2,3,4,5]
n=len(arr)
odd_count,even_count=0,0
for i in range(0,n):
    if(arr[i]%2==0):
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print("the even count is:",even_count)
print("the odd count is:",odd_count)
