class Bag:
    
    color = 'black'   #속성(명사)
    def __init__(self,x):
        self.data=[]
    def add(self):   #기능(동사)
        
        self.data.append(self.data)


handbag = Bag()
print(handbag.color)
handbag.add('핸드폰')
print(handbag.data)

backpack = Bag()
print(backpack.color)
backpack.add('notebook')
print(backpack.data)