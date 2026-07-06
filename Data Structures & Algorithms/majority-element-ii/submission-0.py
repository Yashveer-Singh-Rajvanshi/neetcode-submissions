class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        output = []

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        for key,value in hashmap.items():
            if hashmap[key] > len(nums)/3:
                output.append(key)
            else:
                continue
        
        return output