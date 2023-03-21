import random

choice = 1
while choice == 1:
    rounds = int(input("Rock Paper Scissors!!\nHow many rounds do you want to play:"))
    print("RULES:\nENTER:\nS for Scissors\nR for rock\nP for paper\n")
    win, lose, draw = (0, 0, 0)
    for i in range(0, rounds):
        print(f"ROUND {i + 1}")
        x = str(input("Enter your Choice:"))
        option = ["Rock", "Paper", "Scissors"]
        cho = random.choice(option)
        print(f"The computer Chose {cho}")
        if (x == 'R' or x == 'r' and cho == "Scissors") or (x == 'P' or x == 'p' and cho == "Rock") or (
                x == 'S' or x == 's' and cho == "Paper"):
            win += 1
        elif (x == 'R' or x == 'r' and cho == "Rock") or (x == 'P' or x == 'p' and cho == "Paper") or (
                x == 'S' or x == 's' and cho == "Scissors"):
            draw += 1
        else:
            lose += 1
    if win > (rounds / 2):
        print("YOU WIN!!")
    elif lose > (rounds / 2):
        print("YOU LOSE")
    elif win == lose or draw > (rounds / 2):
        print("Its a DRAW")
    print(f"\nSCORES\nWins:{win} Lost:{lose} Draws:{draw}")
    choice = int(input("\nEnter 1 to Play Again and 0 to Exit"))
