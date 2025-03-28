x = float(input("Enter first number: "))  
y = float(input("Enter second number: "))  
op = input("Enter operation (+, -, *, /): ")  

if op == '+':  
    print("Result:", x + y)  
elif op == '-':  
    print("Result:", x - y)  
elif op == '*':  
    print("Result:", x * y)  
elif op == '/':  
    print("Result:", x / y if y != 0 else "Error! Division by zero.")  
else:  
    print("Invalid operation!")  
