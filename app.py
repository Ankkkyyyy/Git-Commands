

from func import doAddition, doDivision,doSubtraction
from mulfunc import doMul

def main():
    print('Welcome to demo app')
    print(""" \n Select the function from below option\n
          1. Add 
          2. Subtract
          3. Multiply 
          4. Division 
          5. testing 
          """)

    user_input = input('Select the function')
    a = int(input('Enter value of a '))
    b = int(input('Enter value of b '))

    if user_input == '1':
        result = doAddition(a,b)
    elif user_input == '2':
        result = doSubtraction(a,b)
    elif user_input == '3':
        result = doMul(a,b)
    elif user_input == '4':
        result = doDivision(a,b)
    
    print('Result ',result)

if __name__ == '__main__':
    main() 
