def maxMin(k, arr):
    import sys
    arr.sort()
    n=len(arr)
    i=0
    j=k-1
    min_num=sys.maxsize
    while j<n:
        if arr[j]-arr[i]<min_num:
            min_num=arr[j]-arr[i]
        if min_num==0:
            return 0
        i+=1
        j+=1
    return min_num
