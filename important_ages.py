#receive age
age = eval(input("enter age: "))

#condition
if (age >= 1) and (age <= 18):
    print("important Birtday")
elif(age == 21) or (age == 50):
    print("important Birtday")
elif not (age < 65):
    print("important Birtday")
else:
    print("not important")