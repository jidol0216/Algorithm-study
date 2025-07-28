

class Human:



    def __init__(self,age,name):
        self.age = age
        self.name = name

    def intro(self):
        print("나이:",self.age)
        print("이름:",self.name)


kim = Human(29,'김상형')
# print('나이',kim.age)
# print('이름',kim.name)
kim.intro()

lee = Human(45,'이승우')
lee.intro()