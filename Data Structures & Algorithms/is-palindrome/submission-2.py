class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_str = ""

        for ch in s:
            lower_ch = ch.lower()
            
            if (lower_ch >= 'a' and lower_ch <= 'z') or (lower_ch >= "0" and lower_ch <= "9") :
                new_str += lower_ch

        ptr1 = 0
        ptr2 = len(new_str)-1
        is_palindrom = True

        while ptr2 > ptr1:
            if new_str[ptr1] == new_str[ptr2]:
                ptr1 += 1
                ptr2 -= 1
            else:
                is_palindrom = False
                break

        if is_palindrom == True:
            return True
        else:
            return False
        