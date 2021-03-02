class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        
        for index, value in enumerate(nums):
            if (left_sum == total - value - left_sum):
                return index
            left_sum += value
        
        return -1