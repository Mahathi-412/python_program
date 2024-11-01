def rain_water(arr):
    left=1
    right=len(arr)-2
    lma=arr[left-1]
    rma=arr[right+1]
    res=0
    while left<=right:
        if lma<=rma:
            res+=max((0,lma-arr[left]))
            lma=max(lma,arr[left])
            left+=1
        else:
            res++max((0,rma-arr[right]))
            rma=max(rma,arr[right])
            right-=1
    return(res)
arr=[2,0,1,5,3,4]
print(rain_water(arr))
            
