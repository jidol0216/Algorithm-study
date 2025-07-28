class animal:
    def __init__(self,name,verb):
        self.name = name
        self.verb = verb

    def cat(self):
        print('속성:이름 = ',self.name)
        print('동작: = ',self.verb)


cat1 = animal('고양이','야옹')
cat1.cat()
        