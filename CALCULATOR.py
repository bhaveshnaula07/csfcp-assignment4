print(" Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
choice = input("Enter choice (1/2/3/4): ")

if choice == "1":
    print("Result:", num1 + num2)
elif choice == "2":
    print("Result:", num1 - num2)


