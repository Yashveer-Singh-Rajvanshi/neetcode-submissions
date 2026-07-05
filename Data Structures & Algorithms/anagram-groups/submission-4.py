class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        output = []

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in hashmap:
                hashmap[sorted_word] = []
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            for key in hashmap.keys():
                if sorted_word == key:
                    hashmap[key].append(word)
            
        for key in hashmap.keys():
            output.append(hashmap[key])

        return output
        




        