import random 

player = input(f"Enter your move: ").lower()

rpc = ["rock", "paper", "scissors"]
comp_player = random.choice(rpc)
print(f"The computer has chosen: {comp_player}")

if str(player) == 'paper' and str(comp_player) == 'rock':
    print(f"Player Wins!")
elif str(player) == 'rock' and str(comp_player) == 'paper':
    print(f"Computer Wins!")
elif str(player) == 'paper' and str(comp_player) == 'scissors':
    print(f"Computer Wins!")
elif str(player) == 'scissors' and str(comp_player) == 'paper':
    print(f"Player Wins!")
elif str(player) == 'rock' and str(comp_player) == 'scissors':
    print(f"Player Wins!")
elif str(player) == 'scissors' and str(comp_player) == 'rock':
    print(f"Computer Wins!")
elif str(player) == str(comp_player):
    print(f"IT'S A TIE!")
else:
    print("ERROR!")