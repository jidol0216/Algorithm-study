def postfix(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit(): 
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  
    
    return stack[0]

print(postfix("3 4 +"))       
print(postfix("5 1 2 + 4 * + 3 -")) 