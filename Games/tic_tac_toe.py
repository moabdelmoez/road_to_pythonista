"""
High level overview of a game
we need:
- board
- display that board
- play game
- handle turn
- check win
    - check rows
    - check columns
    - check diagonals
- check tie
- flip between players
- 
"""
# ------------Global Variable--------------- # 14

# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"] # 1

# If game is still going
game_still_going = True

# Who won? Or tie?
winner = None

# Whos turn is it
current_player = 'X'

# display board
def display_board(): # 2
  print(board[0] + "|" + board[1] + "|" + board[2])
  print(board[3] + "|" + board[4] + "|" + board[5])
  print(board[6] + "|" + board[7] + "|" + board[8]) 

# play a tic tac toe game
def play_game(): # 4
  # display inial board
  display_board()

  # while the gamse is still going
  while game_still_going: # 8

    # handle a single turn of an arbitrary player
    handle_turn(current_player)

    # check if the game has ended
    check_if_game_over()

    # flip to the other player
    flip_player()
  
  # The game has ended # 13
  if winner == 'X' or winner == 'O':
    print(winner, 'won.')
  elif winner == None:
    print("Tie.")
  
  # handle_turn() # 6

# handle a single turn of an arbitrary player
def handle_turn(player): # 7
  
  print(player + "'s turn.")
  position = input("Choose a position from 1 to 9: ")
  
  valid = False

  # to avoid overwritten on the same posiotion that already occupied
  while not valid:
  
    # handle edge cases, just accept the numbers from 1 to 9
    while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
      position = input("Choose a position from 1 to 9: ")
    
    position = int(position) - 1

    if board[position] == '-':
      valid = True 
    else:
      print('You cannot go there. Go again.')

  board[position] = player

  display_board()


def check_if_game_over(): # 9
  check_for_winner()
  check_if_tie()

def check_for_winner(): # 10

  # set up global variable # 22
  global winner

  # check rows
  row_winner = check_rows() # 18
  # check columns
  column_winner = check_columns() # 19
  # check diagonals
  diagonal_winner = check_diagonals() # 20

  # 21
  if row_winner:
    # there was a win
    winner = row_winner
  elif column_winner:
    # there was a win
    winner = column_winner
  elif diagonal_winner:
    # there was a win
    winner = diagonal_winner
  else:
    # there was no win
    winner = None
  return

def check_rows(): # 15

  # set up golbal variable
  global game_still_going

  # check if any of the rows have all the same value (and not empty)
  row_1 = board[0] == board[1] == board[2] != '-'
  row_2 = board[3] == board[4] == board[5] != '-'
  row_3 = board[6] == board[7] == board[8] != '-'

  # if any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False

  #return a winner (X or O)
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]

  return

def check_columns(): # 16

  # set up golbal variable
  global game_still_going

  # check if any of the columns have all the same value (and not empty)
  column_1 = board[0] == board[3] == board[6] != '-'
  column_2 = board[1] == board[4] == board[7] != '-'
  column_3 = board[2] == board[5] == board[8] != '-'

  # if any column does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False

  #return a winner (X or O)
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]

  return


def check_diagonals(): # 17
  # set up golbal variable
  global game_still_going

  # check if any of the diagonals have all the same value (and not empty)
  diagonal_1 = board[0] == board[4] == board[8] != '-'
  diagonal_2 = board[2] == board[4] == board[6] != '-'

  # if any diagonal does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False

  #return a winner (X or O)
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]

  return


def check_if_tie(): # 11
  
  global game_still_going
  
  if "-" not in board:
    game_still_going = False

  return

def flip_player(): # 12
  
  # set up global variable
  global current_player
  
  # if current player was X, then change to O
  if current_player == 'X':
    current_player = 'O'
  # if current player was O, then change to X
  elif current_player == 'O':
    current_player = 'X'
  return

play_game() # 5


# now we have an empty board, #3
# display_board()
