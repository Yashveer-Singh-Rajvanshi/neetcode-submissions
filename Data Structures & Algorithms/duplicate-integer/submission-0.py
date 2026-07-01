class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_set = set()

        for num in nums:
            new_set.add(num)

        if len(nums) == len(new_set):
            return False
        else:
            return True
        