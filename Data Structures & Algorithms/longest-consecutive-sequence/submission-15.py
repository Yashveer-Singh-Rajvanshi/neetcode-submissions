class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums) 
        longest = 0
        count = 1

        if nums == []:
            return 0

        
        if len(nums) <= 1:
            return 1



        for i in range(len(nums)-1):

            

            if sorted_nums[i+1] == sorted_nums[i] + 1:
                count += 1
            elif sorted_nums[i] == sorted_nums[i+1]:
                pass
            elif sorted_nums[i+1] != sorted_nums[i] + 1:
                count = 1

            longest = max(longest,count)

        return longest 
                
                


        