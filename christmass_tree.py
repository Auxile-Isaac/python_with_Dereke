# Asking the user how tall his tree is going to be
length = eval(input("how tall is your tree?: "))
space = " "
Leaf = "#"
extra_leaf = "##"
Last_one = (space * (length - 1)) + Leaf
while length > 0:
    print(space * (length - 1), Leaf)

    if length > 0:
        Leaf = Leaf + extra_leaf
    length -= 1
    continue
else:
    print(Last_one)


