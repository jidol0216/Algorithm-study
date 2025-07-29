def check_brackets(expression):
    stack = []

    for char in expression:
        if char in "({[":
            stack.append(char)
            print(f"stack = {stack}")

        elif char in ")}]":
            if not stack:
                return False
            top = stack.pop()
            print(f"stack= {stack}")

            
    return len(stack) == 0



print(check_brackets("(a+b)"))