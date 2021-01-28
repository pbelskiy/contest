class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        local_max = 0
        global_max = 0
        
        for n in arr * k:
            local_max = max(n, n + local_max)
            
            if local_max > global_max:
                global_max = local_max
                
        return global_max
 
