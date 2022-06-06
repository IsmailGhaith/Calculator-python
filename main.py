# Adds Function
def add(x, y):
    return x + y

# Subtracts Function
def subtract(x, y):
    return x - y

# Multiplies Function
def multiply(x, y):
    return x * y

# Divides Function
def divide(x, y):
    return x / y


print("Select Operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # input
    choice = input("Enter Your Choice(1-2-3-4):")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter First num:"))
        num2 = float(input("Enter Second num:"))

        # Add
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        # Subtracts
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        # Multiplies
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        # Divide
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # check , break
        next_calculation = input("Let's Do Next Calculation? (yes/no):")
        if next_calculation == "no":
          break

    else:
        print("Invalid Input In Our Choice")