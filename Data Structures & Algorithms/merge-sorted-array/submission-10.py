import random

def quick_sort(nums):

    if len(nums) <= 1:
        return nums

    random_idx = random.randint(0,len(nums)-1)
    nums[random_idx],nums[len(nums)-1] = nums[len(nums)-1],nums[random_idx]

    pivot = len(nums)-1
    j = 0
    i = j-1

    while j != pivot:
        if nums[j]<=nums[pivot]:
            i=i+1
            nums[i],nums[j] = nums[j],nums[i]       
        j+=1

    i+=1
    nums[i],nums[pivot] = nums[pivot],nums[i]

    left_sorted = quick_sort(nums[:i])
    right_sorted = quick_sort(nums[i+1:])

    return left_sorted + [nums[i]] + right_sorted


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = 0
        p2 = 0

        while p1 < len(nums1):

            if p2 > len(nums2)-1:
                break

            if nums1[p1] == 0:
                nums1[p1] = nums2[p2]
                if p2 > len(nums2)-1:
                    continue
                else:
                    p2+=1
            p1+=1
        
        nums1[:] = quick_sort(nums1)

        





