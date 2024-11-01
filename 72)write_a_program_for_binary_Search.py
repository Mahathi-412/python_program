def bin_search(arr,search):
    low=0
    high=len(arr)-1
    while low<high:
        mid=(low+high)//2
        if arr[mid]==search:
            return mid,"found"
        elif arr[mid]>search:
            high=mid-1
        else:
            low=mid+1
    return 1,"not found"
arr=[int(i) for i in input().split(" ")]
arr.sort()
search=5
print(bin_search(arr,search))
    
