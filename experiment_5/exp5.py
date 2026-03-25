class Solution:
    
    def perfectSum(self, arr, target):
        n = len(arr)
        dp = [[-1] * (target + 1) for _ in range(n)]
        
        def solve(idx, target):
            if idx == n:
                return 1 if target == 0 else 0
            
            if dp[idx][target] != -1:
                return dp[idx][target]

            npick = solve(idx + 1, target)

            pick = 0
            if arr[idx] <= target:
                pick = solve(idx + 1, target - arr[idx])
            
            dp[idx][target] = pick + npick
            return dp[idx][target]
        
        return solve(0, target)
