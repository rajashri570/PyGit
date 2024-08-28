class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1
    def push(self,ele):
        if self.is_empty():
            self.top = 0
            self.stack.append(ele)
        else:
            self.top += 1
            self.stack.append(ele)
    def print_stack(self):
        print(self.stack)
    def is_empty(self):
        return len(self.stack) == 0
st = Stack()
st.push(10)
st.push(20)
st.print_stack()
print(st.is_empty())
st2 = Stack()
print(st2.is_empty())