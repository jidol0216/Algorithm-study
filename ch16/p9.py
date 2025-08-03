class Deque:
    def __init__(self):
        self._data = []

    def push_front(self, x):  
        self._data.insert(0, x)

    def push_back(self, x):   
        self._data.append(x)

    def pop_front(self):
        if not self._data:
            return -1
        return self._data.pop(0)

    def pop_back(self):
        if not self._data:
            return -1
        return self._data.pop()

d = Deque()
d.push_back(1)         
d.push_front(2)      
print(d.pop_front())  
print(d.pop_back())    
print(d.pop_back())     
