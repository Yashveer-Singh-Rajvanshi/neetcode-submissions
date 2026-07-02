class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr1 = 0
        ptr2 = 0  # Change 1: 1 ki jagah 0 se shuru kiya taaki IndexError na aaye
        k = 0

        for i in range(len(nums)):
            if ptr2 >= len(nums):
                break
                
            if nums[ptr1] != val:
                ptr1 += 1
                ptr2 = max(ptr2, ptr1) 
                k += 1
            elif nums[ptr2] == val:
                ptr2 += 1
            elif nums[ptr1] == val:  
                nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
                ptr1 += 1
                ptr2 += 1
                k += 1
        
        return k

        
