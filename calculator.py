#this is a simple calcurator that perfom addition, substraction, multiplication and Division
#asking inputs
num1, operator, num2 = input("What's your operation? ").split()

#converting string into integers
num1 = int(num1)
num2 = int(num2)

#calculation logic
if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("use either + , - ,* or /")