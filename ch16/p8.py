class C_Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [0] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, x):
        if self.size == self.capacity:
            return
        self.data[self.tail] = x
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return -1
        val = self.data[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return val

    def front(self):
        if self.size == 0:
            return -1
        return self.data[self.head]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

q = C_Queue(2)

print(q.enqueue(10))  
print(q.enqueue(20))  
print(q.enqueue(30))  
print(q.front())     
print(q.dequeue())    
print(q.enqueue(30))  
print(q.front())      
print(q.is_full())