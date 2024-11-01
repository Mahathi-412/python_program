def slide(arr,k):
    n=len(arr)
    if n<k:
        return "invalid"
    wid_s=sum(arr[:k])
    max_s=wid_s
    for i in range(n-k):
        wid_s=wid_s-arr[i]+arr[i+k]
        max_s=max(wid_s,max_s)
    return max_s
arr=[2,4,3,2,5]
k=2
print(slide(arr,k))
