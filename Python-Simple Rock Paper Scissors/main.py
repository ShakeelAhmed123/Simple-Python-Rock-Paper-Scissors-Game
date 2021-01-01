import random

print("WELCOME TO A GAME OF ROCK PAPER SCISSORS")
print()

operations = ["R", "P", "S", "ROCK", "PAPER", "SCISSOR"]
print("[R]ock, [P]aper or [S]cissors?")
move = input(">").upper()

def game():
    moves = ["ROCK", "PAPER", "SCISSOR"]
    pick_move = random.choice(moves)
    print(f"You picked {move} and I picked {pick_move}")

    if pick_move == "ROCK":
        if move == "ROCK" or "R":
            print("That's a tie! Let's retry!")
        elif move == "SCISSORS" or "S":
            print("I won! Yayyy!")
        elif move == "PAPER" or "P":
            print("You Won! Congrats!")
        else:
            print("Incorrect Move, Please Select [R]ock, [P]aper or [S]cissors!")

    elif pick_move == "PAPER":
        if move == "ROCK" or "R":
            print("I won! Yayyy!")
        elif move == "SCISSORS" or "S":
            print("You Won! Congrats!")
        elif move == "PAPER" or "P":
            print("That's a tie! Let's retry!")
        else:
            print("Incorrect Move, Please Select [R]ock, [P]aper or [S]cissors!")

    elif pick_move == "SCISSOR":
        if move == "ROCK" or "R":
            print("You Won! Congrats!")
        elif move == "SCISSORS" or "S":
            print("That's a tie! Let's retry!")
        elif move == "PAPER" or "P":
            print("I won! Yayyy!")
        else:
            print("Incorrect Move, Please Select [R]ock, [P]aper or [S]cissors!")

    else:
        print("There seem to be some sort of error in the script!")

game()