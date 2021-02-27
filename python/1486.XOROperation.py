class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        i = 0
        result = 0
        while len(nums) < n:
            nums.append(start + 2*i)
            i += 1
        
        for x in nums:
            result ^= x
            
        return result
            