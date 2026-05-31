## BUILD A SIMPLE CALCULATOR [CLI]

num1 = float(input("enter fisrt number "))
num2 = float(input("enter first number "))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("enter your choice(1-4) ")

if choice == "1":
    print("Result =", num1 + num2)
elif choice == "2":
    print("Result =", num1 - num2)
elif choice == "3":
    print("Result =", num1 * num2)
elif choice == "4":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Division by zero is not alllowed ")
else:
    print("invalid choice ")

    