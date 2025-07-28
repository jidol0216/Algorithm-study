

# class MyIterator:
#     def __init__(self,data):
#         self.data=data
#         self.position = 0
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.position >= len(self.data):
#             raise StopIteration
#         result = self.data[self.position]
#         self.position +=1
#         return result
    
# if __name__ == "__main__":
#     fruits = ["apple", "banana", "cherry"]
#     a = MyIterator(fruits)
    
#     for i in a:
#         print(i)

# nums = iter(range(10))
# for i in nums:
#     print(i**2) 



# class MyIterator:
#     def __init__(self,data):
#         self.data = data
#         self.position = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.position >= len(self.data):
#             raise StopIteration
#         result = self.data[self.position]
#         self.position+=1
#         return result
    
# a = MyIterator(range(10))
# for i in a:
#     print(i**2)


class MyRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None: 
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        self.step = step
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        result = self.current
        self.current += self.step
        return result

for i in MyRange(3):
    print(i, end=' ')