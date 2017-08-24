"""
List TODO:
- make more battleships
- make battleships in size
- something more
"""

from random import randint

board = []

def ocean_size(num_p):
  if num_p == 1:
    for x in range(0, 5):
      board.append(["O"] * 5)
  elif num_p == 2:
    for x in range(0, 7):
      board.append(["O"] * 7)
  else:
    for x in range(0, 1):
      board.append(["O"] * 1)

def print_board(board):
  for row in board:
    print (" ".join(row))

print ("Hi! Let's play battelship")
num_player = int(input("Enter the number or players - 1 or 2: "))
ocean_size(num_player)
print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row)
print (ship_col)

if num_player == 1:
  for turn in range(4):
    print ("Turn", turn + 1)
    guess_row = int(input("Guess Row: ")) - 1
    guess_col = int(input("Guess Col: ")) - 1

    if guess_row == ship_row and guess_col == ship_col:
      print ("Congratulations! You sank my battleship!")
      break
    else:
      if guess_row not in range(5) or guess_col not in range(5):
        print ("Oops, that's not even in the ocean.")
      elif board[guess_row][guess_col] == "X":
        print ("You guessed that one already.")
      else:
        print ("You missed my battleship!")
        board[guess_row][guess_col] = "X"
    if (turn == 3):
      print ("Game Over")
    print_board(board)
      
elif num_player == 2:
  for turn in range(8):
    print ("Turn", turn + 1)
    if turn % 2 == 0:
      print ("The turn of the first player")
    else:
      print ("The turn of the second player")
    guess_row = int(input("Guess Row: ")) - 1
    guess_col = int(input("Guess Col: ")) - 1

    if guess_row == ship_row and guess_col == ship_col:
      if turn % 2 == 0:
        print ("Congratulations of 1st player! You sank my battleship!")
        break
      else:
        print ("Congratulations for 2nd player! You sank my battleship!")
        break
    else:
      if guess_row not in range(7) or guess_col not in range(7):
        print ("Oops, that's not even in the ocean.")
      elif board[guess_row][guess_col] == "X":
        print( "That one was guessed already." )
      else:
        print ("You missed my battleship!")
        board[guess_row][guess_col] = "X"
      if (turn == 7):
        print ("Game Over")
      print_board(board)
else:
  print ("Something went wrong. Bye")
  