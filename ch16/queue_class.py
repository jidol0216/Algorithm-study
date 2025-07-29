class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,data):
        self.queue.append(data)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return 
    
    def is_empty(self):
        return len(self.queue) == 0
            