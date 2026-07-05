import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums

        random_idx = random.randint(0,len(nums)-1)
        nums[len(nums)-1],nums[random_idx] = nums[random_idx],nums[len(nums)-1]

        pivot = len(nums)-1
        j = 0
        i = j - 1

        while j < pivot:
            if nums[j] <= nums[pivot]:
                i += 1
                nums[i],nums[j] = nums[j],nums[i]
            j += 1

        i += 1
        nums[i],nums[pivot] = nums[pivot],nums[i]

        left_sorted = self.sortArray(nums[:i])
        right_sorted = self.sortArray(nums[i+1:])

        return left_sorted + [nums[i]] + right_sorted 










        