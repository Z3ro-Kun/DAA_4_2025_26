class Solution:
	def tsp(self, cost):
		n = len(cost)
        INF = float('inf')
        
        dp = [[INF] * n for _ in range(1 << n)]
        dp[1][0] = 0
        
        for mask in range(1 << n):
            for u in range(n):
                if mask & (1 << u):
                    for v in range(n):
                        if not (mask & (1 << v)):
                            new_mask = mask | (1 << v)
                            dp[new_mask][v] = min(
                                dp[new_mask][v],
                                dp[mask][u] + cost[u][v]
                            )
        
        ans = INF
        for i in range(n):
            ans = min(ans, dp[(1 << n) - 1][i] + cost[i][0])
        
        return ans
