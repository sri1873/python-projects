# 1st program(if condition)
x = int(input("Enter a number: "))
if x == 5:
    print("Equals 5")
if x > 4:
    print("Greater than 4")
if x >= 5:
    print("Greater than or equal to 5")
if x < 6:
    print("Less than 6")
if x <= 5:
    print("Less than or equal to 6")
if x != 6:
    print("It is not equal to 6")

# 2nd program(if indentation)
x = 5
print("Before 5")
if x == 5:
    print("Is 5")
    print("Is still 5")
    print('Third 5')
print("After 5")
print("Before 6")
if x == 6:
    print("Is 6")
    print("Is still 6")
    print('Third 6')
print("After 6")

# 3 program(nested if)
x = 500
if x > 1:
    print("More than 1")
    if x < 100:
        print("Less than 100")
print("All Done")

# 4 Program(if else)
x = -2
if x > 2:
    print("Bigger")
else:
    print("Smaller")
print("All done")

# 5 Program(Elif Multi-way)
x = 20
if x < 2:
    print("small")
elif x < 10:
    print("Medium")
else:
    print("Large")
print("All done")

# Multi-Way Puzzles
x = -2
if x < 2:
    print('Below 2')
elif x >= 2:
    print('Two or more')
else:
    print('Something else')
x = 20
if x < 2:
    print('Below 2')
elif x < 20:
    print('Below 20')
elif x < 10:
    print('Below 10')
else:
    print('Something else')
