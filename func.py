

def doAddition(a:int,b:int):
    return a+b

def doSubtraction(a:int,b:int):
    return a-b

def doDivision(a:int,b:int):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cant divide by zero"  

