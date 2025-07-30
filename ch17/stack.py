class MyStack:

    def __init__(self):
        self.stack =[]
        self.top_index = -1

    def is_empty(self):
        return self.top_index == -1
    
    def push(self,data):
        self.stack= self.stack[:self.top_index+1] +[data]
        self.top_index +=1
    
    def pop(self):
        if self.is_empty():
            return None
        data = self.stack[self.top_index]
        self.top_index -=1
        return data
    
    def top(self):
        if self.is_empty():
            return None
        return self.stack[self.top_index]
    
    def status(self):
        return self.stack
st = MyStack()

st.push(3)
st.push(2)
st.push(1)
print(st.pop())