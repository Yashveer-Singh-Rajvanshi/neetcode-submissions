class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i = 0
        j = 2
        substring = ""

        while j < len(num):
            if num[i] != num[i+1] or num[i+1] != num[i+2]:
                pass
            
            if num[i] == num[i+1] == num[i+2]:
                if substring == "" or int(substring) < int(num[i:j+1]):
                    substring = num[i:j+1]
            
            i+=1
            j+=1
        
        return substring
        