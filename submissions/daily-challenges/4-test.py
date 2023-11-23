print(f"!! ROCK PAPER SCISSORS GAME !!")

player1 = input(f"Player One, enter your move: ")
player2 = input(f"Player Two, enter your move: ")

if str(player1) == 'PAPER' and str(player2) == 'ROCK':
    print(f"Player 1 Wins!")
elif str(player1) == 'ROCK' and str(player2) == 'PAPER':
    print(f"Player 2 Wins!")
elif str(player1) == 'PAPER' and str(player2) == 'SCISSORS':
    print(f"Player 2 Wins!")
elif str(player1) == 'SCISSORS' and str(player2) == 'PAPER':
    print(f"Player 1 Wins!")
elif str(player1) == 'ROCK' and str(player2) == 'SCISSORS':
    print(f"Player 1 Wins!")
elif str(player1) == 'SCISSORS' and str(player2) == 'ROCK':
    print(f"Player 2 Wins!")
elif str(player1) == str(player2):
    print(f"IT'S A TIE!")
else:
    print("ERROR!")
