while True:
    
    class Calculator:
        def __init__(self):
            self.number1 = None
            self.number2 = None
        def input_numbers(self):
            self.number1 = float(input("Enter the first number please: "))
            self.number2 = float(input("Enter the second number please:"))
        def addition(self):
            return self.number1 + self.number2
        def subtraction(self):
            return  self.number1 - self.number2
        def multiplication(self):
            return self.number1 * self.number2
        def division(self):
            return self.number1 / self.number2
    calculator = Calculator()
    calculator.input_numbers()
    functionality= input("Choose a function (+,-,*,/) ")

    result= None

    if functionality == '+':
        result = calculator.addition()
    elif functionality == '-':
        result = calculator.subtraction()
    elif functionality == '*':
        result = calculator.multiplication()
    elif functionality == '/':
        result= calculator.division()
    else:
        result= "Invalid function"
        exit()

    print("Your result is, result ", result)
