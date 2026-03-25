class Solution:
    
    def longestSubarray(self, arr, k):
        mp = {}
        prefix = 0
        max_len = 0
        
        for i in range(len(arr)):
            prefix += arr[i]
            
            if prefix == k:
                max_len = i + 1
            
            if (prefix - k) in mp:
                max_len = max(max_len, i - mp[prefix - k])
            
            if prefix not in mp:
                mp[prefix] = i
        
        return max_len
