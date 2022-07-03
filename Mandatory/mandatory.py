
def post_fix(expression):
    
    split_expression = expression.split()
    print (split_expression)
    
    stack = []
    result = None
    
    for element in split_expression:
        if element in "0123456789":
            stack.append(float(element))
        elif element == "-":
            number2 = stack.pop()
            result = stack.pop() - number2
        elif element == "+":
            result = stack.pop() + stack.pop()
        elif element == "*":
            result = stack.pop() * stack.pop()
        elif element == "/":
            number2 = stack.pop()
            result = stack.pop() / number2
        
        if not (result == None):
            stack.append(result)
            result = None
            
    return stack
        

print(post_fix("6 8 / 5 /"))
print(post_fix("8 7 2 / - 3 + 4 -"))
print(post_fix("8 5 + 9 4 / - "))
print(post_fix("8 7 3 * 4 * - 6 +"))
print(post_fix("4 5 9 / 6 * + 7 - "))
