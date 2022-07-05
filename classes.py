# ask age
age = eval(input("enter age: "))
if age < 5:
    print("too young for school ")
elif age == 5:
    print("go to kindergarten")
elif (age >= 6) and (age <= 17):
    grade = age - 5
    print(f"go to grade {grade}")
else:
    print("go to college")
