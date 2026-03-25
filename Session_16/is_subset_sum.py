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
        dp=[[False for _ in range(sum+1)] for __ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=True
        for i in range(1, n+1):
            for j in range(1, sum+1):
                if arr[i-1]<=j:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][sum]
