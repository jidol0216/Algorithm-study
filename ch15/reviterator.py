#입력 데이터를 역순으로 출력하는 클래스 생성

class ReverseIterator:
    def __init__(self,data):
        self.data =data
        self.position = len(self.data) -1 
    def __iter__(self):
        return self
    def __next__(self):
        if self.position <0:
            raise StopIteration
        result =self.data[self.position]
        self.position -= 1
        return result
    
if __name__ in "__main__":
    i = ReverseIterator([1,2,3])
    for item in i:
        print(item)
    print(next(i))