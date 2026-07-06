class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        for i in range(0,len(nums)):
            count = 1
            current_num = nums[i]

            while current_num+1 in nums:
                count += 1
                current_num += 1
                 
            longest = max(longest,count)

        return longest       
                
                


        