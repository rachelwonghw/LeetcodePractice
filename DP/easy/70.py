# top down approach
class Solution:
    def climbStairs(self, n: int, arr = {}) -> int:
        
        if n in arr:
            return arr[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        arr[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
        return arr[n]