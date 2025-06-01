#  This function adds two numbers 
def add(x, y):
    return x + y
# This function subtracts two numbers
def subtract(x, y):
    return x - y
#This function multiplies two numbers
def multiply(x, y):
    return x * y
# This function devides two numbers
def devide(x, y):
    return x / y
print("Select operation.")
print("1. Add")
print("2. Subtact")
print("3. Multiply")
print("4. Devide")

while True:
    #take input form the user
    choice = input("Enter choice(1/2/3/4): ")

    #check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter frist number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input, please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        
        elif choice == '2':
            print(num1, '-', num2, '=', subtract(num1, num2))

        elif choice == '3':
            print(num1, '*', num2, '=', multiply(num1, num2))

        elif choice == "4":
            print(num1, '/', num2, '=', devide(num1, num2))

        #check if user wants another calculation
        # break the while loop if the answer is no
        next_calculation = input("Let's do next calcultion? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")