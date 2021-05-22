class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 0
        curr = 0 
        
        for item in nums:
            if nums[curr] == nums[unique]:
                curr = curr + 1
            else:
                unique = unique + 1
                nums[unique] = nums[curr]
                curr = curr + 1
        
        
        return unique + 1