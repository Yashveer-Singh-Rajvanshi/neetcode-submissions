class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []
        product = 1

        p1 = 0
        a = 0

        while a < len(nums):
            if a == p1:
                p1+=1
            else:
                product = product*nums[p1]
                p1+=1
            
            if p1 == len(nums):
                output.append(product)
                product = 1
                a+=1
                p1=0

        return output
                    
