def two_sum(arr):
    tar=6
    low=0
    high=len(arr)-1
    while(low<high):
        if arr[low]+arr[high]>tar:
            high-=1
        elif arr[low]+arr[high]<tar:
            low+=1
        else:
            return low,high
arr=[2,5,4,9]
print(two_sum(arr))
