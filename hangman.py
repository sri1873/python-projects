import random
from words import words
from words import lives_visual_dict
import string


def get_valid_word():
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    lives = 7
    word = get_valid_word()
    all_letters = set(string.ascii_uppercase)
    word_letters = set(word)
    used_letters = set()
    while len(word_letters) > 0 and 0 < lives:
        print("You have ", lives, " left These are the letters that you have guessed", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(lives_visual_dict[lives])
        print("The word:", ' '.join(word_list))
        guess = str(input("Guess a letter").upper())
        if guess in all_letters - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
                if len(word_letters) == 0:
                    answer = [_ for _ in word]
                    print(' '.join(answer))
            else:
                lives -= 1
                print(f"lost one life your letter is not in the word")
        elif guess in used_letters:
            print("YOU TRIED THAT ALREADY PLEASE TRY A DIFFERENT LETTER")
        else:
            print("INVALID LETTER.TRY AGAIN")
    if lives == 0:
        print(lives_visual_dict[lives])
        print("You died,the word was ", word)
    else:
        print("You Win!! You guessed the word ", word)


print("Welcome to HANGMAN")
choice = 1
while choice==1:
    hangman()
    choice=int(input(("press 1 to try again 0 to exit")))
    
