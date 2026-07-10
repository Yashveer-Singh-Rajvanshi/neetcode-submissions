class Solution:
    def rotate(self, nums: List[int], k: int) -> None:  
        k = k % len(nums)
        i = 0
        j = len(nums) - 1

        while i<j:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1
            
        a = 0
        b = k-1

        while a<b:
            nums[a],nums[b] = nums[b],nums[a]
            a+=1
            b-=1
            
        c = k
        d = len(nums)-1

        while c<d:
            nums[c],nums[d] = nums[d],nums[c]
            c+=1
            d-=1

            