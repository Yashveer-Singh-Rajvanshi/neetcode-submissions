class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        copynums = nums.copy()
        ansnums = nums + copynums
        return ansnums
         
        