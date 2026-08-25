# Calculator
def add():
    a = int(input("Enter the 1st number: "))
    b = int(input("Enter the 2nd number: "))
    print("The sum of two numbers is:", a + b)

def sub():
    a = int(input("Enter the 1st number: "))
    b = int(input("Enter the 2nd number: "))
    print("The difference of two numbers is:", a - b)

def mul():
    a = int(input("Enter the 1st number: "))
    b = int(input("Enter the 2nd number: "))
    print("The product of two numbers is:", a * b)

def div():
    a = int(input("Enter the 1st number: "))
    b = int(input("Enter the 2nd number: "))
    if b == 0:
        print("Error: Cannot divide by zero!")
    else:
        print("The quotient of two numbers is:", a / b)

class CorrectOptionException(Exception):
    pass

choice = 'y'
while choice.lower() == 'y':
    try:
        oper = int(input("Enter the required operation to be performed:\n1.Addition 2.Subtraction 3.Multiplication 4.Division\n"))
        
        if oper < 1 or oper > 4:
            raise CorrectOptionException("Select a Correct Operation (1-4)")
        
        if oper == 1:
            add()
        elif oper == 2:
            sub()
        elif oper == 3:
            mul()
        elif oper == 4:
            div()
            
    except CorrectOptionException as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Please enter a valid integer")
    
    choice = input("\nDo you want to perform another operation? (y/n): ")
    if choice.lower() == 'n':
        print("Thank you for using the calculator")
        break
    else:
        continue
