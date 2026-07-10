class Solution:
    def rotate(self, nums: List[int], k: int) -> None:  
        n = len(nums)
        k = k % n      
        i = 0
        j = n - k 
        output = []

        for a in range(j,n):
            output.append(nums[a])

        for b in range(i,j):
            output.append(nums[b])

        nums[:] = output


            