class stack:
    def __init__(self):
        self.st = []
    
    def push(self,number):
        self.st.append(number)
    
    def pop(self):
        if len(self.st) == 0:
            return -1
        x = self.st[-1]
        self.st.pop()
        return x

    def top(self):
        if len(self.st) == 0:
            return -1
        return self.st[-1]
    
    def size(self):
        return len(self.st)
    
    def show(self):
        print(self.st)

    def len(self):
        return len(self.st)


class Solution(object):
    def isValid(self, s):
        st = stack()

        for i in range(len(s)):

            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                st.push(s[i])

            if s[i] == ")":
                if st.top() == "(":
                    st.pop()
                else:
                    return False
            elif s[i] == "]":
                if st.top() == "[":
                    st.pop()
                else:
                    return False
            elif s[i] == "}":
                if st.top() == "{":
                    st.pop()
                else:
                    return False
        

        if st.len() == 0:
            return True
        else:
            return False
        