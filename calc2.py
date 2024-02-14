def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x*y
def divide(x, y):
    return x/y

def calculator():
    print('Inputs?')
    temp2 = input()
    x = temp2.split(None, 1)
    y = temp2.split(temp2,1)
    print('add, subtract, multiply, or divide?')
    result = 0
    temp = input()
    if (temp == 'add'):
        result = add(x,y)
    if(temp == 'subtract'):
        result = subtract(x,y)
    if(temp == 'multiply'):
        result = multiply(x,y)
    if(temp == 'divide'):
        result = divide(x,y)
    print(str(result))
calculator()
