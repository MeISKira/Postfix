def math(num2, num1, operation):
    if operation == '+': return int(num2) + int(num1)
    elif operation == '-': return int(num2) - int(num1)
    elif operation == '/': return int(num2) / int(num1)
    elif operation == '*': return int(num2) * int(num1)
def postFix(expr):
    stack = []
    for step in str(expr).split():
        if step.isnumeric():
            stack.append(step)
        else:
            num2 = stack[0]
            stack.remove(num2)
            num1 = stack[0]
            stack.remove(num1)
            result = math(num2, num1, step)
            # print(result)
            stack.append(int(result))
    return stack[0]

user_input = input('Enter Postfix >> ').strip()
print(postFix(user_input))