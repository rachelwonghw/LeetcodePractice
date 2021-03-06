## linear time complexity
class Solution1:
    def search(self, nums: List[int], target: int) -> int:

        pivot = -1
        for i in range(0, len(nums)):
            if nums[i] == target:
                pivot = i 
            
        return pivot

## log N time complexity done with binary search
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] >= nums[l]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target <= nums[r] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
                
        return -1