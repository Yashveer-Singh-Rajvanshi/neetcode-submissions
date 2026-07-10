class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 1
        while p1<=len(nums)-1:
            if nums[p1] == nums[p1-1]:
                nums.remove(nums[p1])
                p1-=1
            p1 +=1

        count = 0

        for i in range(len(nums)):
            count+=1
        
        return count
            

        
       

            
