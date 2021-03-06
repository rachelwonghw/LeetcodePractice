class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 3 pointer method and start checking from the back of the array
        count1 = m - 1
        count2 = n - 1
        pointer = m + n - 1
        
        while pointer >= 0:
            if count2 < 0:
                break
            if count1 >= 0 and nums1[count1] > nums2[count2]:
                nums1[pointer] = nums1[count1]
                count1 -= 1
                pointer -= 1
            else:
                nums1[pointer] = nums2[count2]
                count2 -= 1
                pointer -= 1
            
        return