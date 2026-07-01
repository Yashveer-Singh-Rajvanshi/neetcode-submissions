class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            miss_num = target - nums[i]
            if miss_num in nums and nums.index(miss_num) != i:
                if nums.index(miss_num) > i:
                    return [i,nums.index(miss_num)]
                else:
                    return [nums.index(miss_num),i]
        