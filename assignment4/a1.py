class Stack:
    def __init__(self, initial_list=None):
        if initial_list is None:
            self.items = []
        else:
            self.items = initial_list

    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def __str__(self):
        return str(self.items)


stack = Stack(['두산', '로키', '부트'])


stack.push('캠프')
print(stack) 
stack.pop()
print(stack) 