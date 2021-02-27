class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[0:counter+1]) for counter in range(len(nums))]