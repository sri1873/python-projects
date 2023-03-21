import random
import winsound

freq = 2000
dur = 1000


def guess(x):
    print(f"Think of a number between 1 to{x}")
    attempts = 0
    low = 1
    high = x
    check = ''
    while check != 'c':
        if high != low:
            comp_guess = random.randint(low, high)
        else:
            comp_guess = low
        check = str(input(f"Is your number {comp_guess}? Press h if I guessed higher; l if too low; c if correct"))
        attempts += 1
        if check == 'h' or check == 'H':
            high = comp_guess - 1
        elif check == 'l' or check == 'L':
            low = comp_guess + 1
    winsound.Beep(freq, dur)
    print(f"YAY I guessed it right in {attempts} attempts")


choice = str(input("e for easy\nm for medium\nh for hard\n"))
if choice == 'e' or choice == 'E':
    guess(10)
if choice == 'm' or choice == 'M':
    guess(25)
if choice == 'h' or choice == 'H':
    guess(50)
