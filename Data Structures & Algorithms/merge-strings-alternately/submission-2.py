class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans_str = ""
        toggle = True

        larger_str = ""
        if len(word1) > len(word2):
            larger_str = word1
        elif len(word1) == len(word2):
            larger_str = word1
        else:
            larger_str = word2
 
        p1 = 0
        p2 = 0

        for i in range(0,len(larger_str)):
            if i > len(word1)-1:
                pass
            else:
                ans_str += word1[p1]
                p1+=1

            if i > len(word2)-1:
                pass
            else:
                ans_str += word2[p2]
                p2+=1
        
        return ans_str



        