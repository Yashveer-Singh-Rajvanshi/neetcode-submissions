class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for idx,num in enumerate(nums):
            miss_value = target - num
            if miss_value in hashmap:
                return [hashmap[miss_value],idx]
            hashmap[num] = idx
            
                    

           
            
            
            
            
        