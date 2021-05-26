class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxArea = 0
        
        pointer1 = 0
        pointer2 = len(height) - 1
        
        if not height: return 0
        
        while pointer1 < pointer2 and 0 <= pointer2 < len(height) and 0 <= pointer1 < len(height):
            maxArea = max(min(height[pointer1], height[pointer2])*(pointer2 - pointer1), maxArea)
            if height[pointer1] > height[pointer2]:
                pointer2 -= 1
            else:
                pointer1 += 1
                
        return maxArea