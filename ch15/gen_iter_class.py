class MyIterator:
    def __init__(self):
        self.data = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        result = self.data * self.data
        if self.data >= 100:
            raise StopIteration
        self.data += 1
        return result
    

