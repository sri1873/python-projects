import random


def guess(x):
    the_number = random.randint(1, x)
    user_input = 0
    attempts = 0
    while user_input != the_number:
        user_input = int(input(f"Enter a number between 1 to {x}:"))
        if user_input > the_number:
            print("Sorry Try Again.Too High")
            attempts += 1
        elif user_input < the_number:
            print("Sorry Try Again.Too Low")
            attempts += 1
    attempts += 1
    print(f"YAY!! You Guessed right\nYou guessed in {attempts} attempts")


print("Welcome to Guessing the Number")
choice = 1
while choice == 1:
    level = str(input("Enter:\ne for easy\nm for medium\nh for hard level\n"))
    if level == 'e' or level == 'E':
        print("Playing Easy mode")
        guess(10)
    elif level == 'm' or level == 'M':
        print("Playing Medium mode")
        guess(25)
    elif level == 'h' or level == 'H':
        print("Playing Hard mode")
        guess(50)
    choice = int(input("Press 1 to Play again and 0 to Exit"))
