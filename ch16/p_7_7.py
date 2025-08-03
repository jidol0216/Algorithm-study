class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, x: int) -> None:
        self._data.append(x)

    def dequeue(self) -> int:
        if self.is_empty():
            return -1
        return self._data.pop(0) 

    def front(self) -> int:
        if self.is_empty():
            return -1
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0


q = Queue()
print(q.is_empty())  
q.enqueue(5)
q.enqueue(7)
print(q.front())    
print(q.dequeue())   
print(q.dequeue())   
print(q.dequeue())  
