class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        longest = 1

        if len(nums) == 1:
            return 1

        if nums == []:
            return 0

        for num in nums:
            nums_set.add(num)

        for num in nums_set:
            if num-1 not in nums_set:
                x = num
                count = 1
                while x+1 in nums_set:
                    count += 1
                    x = x+1
                longest = max(longest,count)
                
        return longest

        