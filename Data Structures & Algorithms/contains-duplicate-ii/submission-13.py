class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        j = i+1

        while i<len(nums)-1:
           
            if nums[i] == nums[j]:
                if abs(i-j) <= k:
                    return True

            if j == len(nums)-1:
                i+=1
                j = i+1
            else:
                j+=1
            
        return False
        