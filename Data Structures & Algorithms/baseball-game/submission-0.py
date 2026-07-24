class Stack:
    def __init__(self):
        self.st = []
    
    def push(self,num):
        self.st.append(num)
    
    def pop(self):
        return self.st.pop()
    
    def top(self):
        return self.st[-1]
    
    def len(self):
        return len(self.st)
        
    def show(self):
        print(self.st)


class Solution(object):
    def calPoints(self, ops):
        st = Stack()

        for i in range(len(ops)):
            if ops[i] == "C":
                st.pop()
            elif ops[i] == "D":
                Top = st.top()
                st.push(Top*2)
            elif ops[i] == "+":
                st.push(st.st[-1]+st.st[-2])
            else:
                st.push(int(ops[i]))

        sum = 0
        for i in range(st.len()):
            sum = sum + st.st[i]
        
        return sum
        