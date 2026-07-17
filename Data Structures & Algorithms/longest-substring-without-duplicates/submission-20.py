class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        count = 0
        i = 0
        j = 0

        while j<len(s):
            while s[j] in hashset:
                hashset.remove(s[i])
                i+=1
            
            hashset.add(s[j])
            count = max(count,j-i+1)
            j+=1

        return count

        