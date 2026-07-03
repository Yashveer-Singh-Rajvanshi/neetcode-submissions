class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        output = [1] * n
        prefix = [1] * n
        suffix = [1] * n

        prefix[0] = 1
        suffix[len(nums)-1] = 1

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]

        for j in reversed(range(0,len(nums)-1)):
            suffix[j] = suffix[j+1] * nums[j+1]

        for k in range(0,len(nums)):
            output[k] = prefix[k]*suffix[k]

        return output                    
