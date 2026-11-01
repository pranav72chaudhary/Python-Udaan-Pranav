# Simple Calculator

print("Simple Calculator")

nm1 = float(input("Enter number One : "))
nm2 = float(input("Enter Second Number: "))
operator = input("Enter operator : ")

# if-Ladder

if operator == "+":
    print("Addition =", nm1 + nm2)

elif operator == "-":
    print("Subtraction =", nm1 - nm2)

elif operator == "*":
    print("Multiplication =", nm1 * nm2)

elif operator == "/":
    if nm2 == 0:
        print("Cannot divide by zero")
    else:
        print("Division =", nm1 / nm2)

elif operator == "%":
    if nm2 == 0:
        print("Cannot find remainder with zero")
    else:
        print("Remainder =", nm1 % nm2)

elif operator == "**":
    print("Power =", nm1 ** nm2)

else:
    print("Enter valid operator")