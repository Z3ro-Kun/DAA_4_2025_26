class Solution:
    
    def knapsack1D(self, W, val, wt):
        n = len(val)
        dp = [0] * (W + 1)
        
        for i in range(n):
            for w in range(W, wt[i] - 1, -1):
                dp[w] = max(dp[w], val[i] + dp[w - wt[i]])
        
        return dp[W]



class Solution:
    
    def knapSack2D(self, W, val, wt):
        n = len(val)
        dp = [[0] * (W + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for w in range(W + 1):
                if wt[i - 1] <= w:
                    dp[i][w] = max(
                        dp[i - 1][w],
                        val[i - 1] + dp[i - 1][w - wt[i - 1]]
                    )
                else:
                    dp[i][w] = dp[i - 1][w]
        
        return dp[n][W]
