class Solution:
    def isSubsetSum (self, arr, sum):
        if sum in arr:
            return True
        n=len(arr)
        arr.sort()
        for i in range(n):
            if arr[i]>sum:
                arr=arr[0:i]
                break
        n=len(arr)
        if n==0:
            return False

        def solve(arr, i, sum, curr):
            if sum==curr:
                return True
            if i>=len(arr):
                return False
            if sum<curr:
                return False
            if solve(arr, i+1, sum, arr[i]+curr):
                return True
            return solve(arr, i+1, sum,curr)
            
        return solve(arr, 0, sum, 0)
