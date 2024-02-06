#Pseudo Codes
import enum

def swap(board):

  for i in range(len(board)):
    if board[i] == 'W':
      board[i] = 'B'
    elif board[i] == 'B':
      board[i] = 'W'
  return board


class Pieces(enum.Enum):
  a0 = 0
  d0 = 1
  g0 = 2
  b1 = 3
  d1 = 4
  f1 = 5
  c2 = 6
  e2 = 7
  b3 = 8
  c3 = 9
  e3 = 10
  f3 = 11
  g3 = 12
  c4 = 13
  d4 = 14
  e4 = 15
  b5 = 16
  d5 = 17
  f5 = 18
  a6 = 19
  d6 = 20
  g6 = 21

# Following the left right front back convention in naming neighbours

def neighbors(i):

  if i == 0: #a0
      return [Pieces.a6.value, Pieces.d0.value, Pieces.b1.value]

  if i == 1: #d0
      return [Pieces.a0.value, Pieces.g0.value, Pieces.d1.value]

  if i == 2: #g0
      return [Pieces.d0.value, Pieces.g3.value, Pieces.f1.value]

  if i == 3: #b1
      return [Pieces.b3.value, Pieces.d1.value, Pieces.c2.value, Pieces.a0.value]

  if i == 4: #d1
      return [Pieces.b1.value, Pieces.f1.value, Pieces.d0.value]

  if i == 5: #f1
      return [Pieces.d1.value, Pieces.f3.value, Pieces.e2.value, Pieces.g0.value]

  if i == 6: #c2
      return [Pieces.c3.value, Pieces.e2.value, Pieces.b1.value]

  if i == 7: #e2
      return [Pieces.c2.value, Pieces.e3.value, Pieces.f1.value]

  if i == 8: #b3
      return [Pieces.b5.value, Pieces.b1.value, Pieces.c3.value]

  if i == 9: #c3
      return [Pieces.c4.value, Pieces.c2.value, Pieces.b3.value]

  if i == 10: #e3
      return [Pieces.e2.value, Pieces.e4.value, Pieces.f3.value]

  if i == 11: #f3
      return [Pieces.f1.value, Pieces.f5.value, Pieces.e3.value, Pieces.g3.value]

  if i == 12: #g3
      return [Pieces.g0.value, Pieces.g6.value, Pieces.f3.value]

  if i == 13: #c4
      return [Pieces.d4.value, Pieces.c3.value, Pieces.b5.value]

  if i == 14: #d4
      return [Pieces.e4.value, Pieces.c4.value, Pieces.d5.value]

  if i == 15: #e4
      return [Pieces.e3.value, Pieces.d4.value, Pieces.f5.value]

  if i == 16: #b5
      return [Pieces.d5.value, Pieces.b3.value, Pieces.c4.value, Pieces.a6.value]

  if i == 17: #d5
      return [Pieces.f5.value, Pieces.b5.value, Pieces.d4.value, Pieces.d6.value]

  if i == 18: #f5
      return [Pieces.f3.value, Pieces.d5.value, Pieces.e4.value, Pieces.g6.value]

  if i == 19: #a6
      return [Pieces.d6.value, Pieces.a0.value, Pieces.b5.value]

  if i == 20: #d6
      return [Pieces.g6.value, Pieces.a6.value, Pieces.d5.value]

  if i == 21: #g6
      return [Pieces.g3.value, Pieces.d6.value, Pieces.f5.value]

# To check if the move will make a mill ( 3 in a row )
def calc_mill(j, board):

  C = board[j]

  if C == 'x':
    return False

  if j == 0: # Mill check for a0 
    
    if( (board[Pieces.d0.value] == C and board[Pieces.g0.value] == C) or (board[Pieces.b1.value] == C and board[Pieces.c2.value] == C)):
      return True
    else:
      return False
  
  if j == 1: # Mill check for d0
    
    if(board[Pieces.a0.value] == C and board[Pieces.g0.value] == C):
      return True
    else:
      return False
  
  if j == 2: # Mill check for g0
    
    if( (board[Pieces.d0.value] == C and board[Pieces.a0.value] == C) or (board[Pieces.g3.value] == C and board[Pieces.g6.value] == C) or (board[Pieces.f1.value] == C and board[Pieces.e2.value] == C)):
      return True
    else:
      return False

  if j == 3: # Mill check for b1
    
    if( (board[Pieces.a0.value] == C and board[Pieces.c2.value] == C) or (board[Pieces.b3.value] == C and board[Pieces.b5.value] == C) or (board[Pieces.d1.value] == C and board[Pieces.f1.value] == C)):
      return True
    else:
      return False

  if j == 4:  # Mill check for d1
    
    if( board[Pieces.b1.value] == C and board[Pieces.f1.value] == C ):
      return True
    else:
      return False

  if j == 5: # Mill check for f1
    
    if( (board[Pieces.e2.value] == C and board[Pieces.g0.value] == C) or (board[Pieces.b1.value] == C and board[Pieces.d1.value] == C) or (board[Pieces.f3.value] == C and board[Pieces.f5.value] == C)):
      return True
    else:
      return False

  if j == 6: # Mill check for c2
    
    if( (board[Pieces.b1.value] == C and board[Pieces.a0.value] == C) or (board[Pieces.c3.value] == C and board[Pieces.c4.value] == C)):
      return True
    else:
      return False

  if j == 7: # Mill check for e2
    
    if( (board[Pieces.f1.value] == C and board[Pieces.g0.value] == C) or (board[Pieces.e3.value] == C and board[Pieces.e4.value] == C)):
      return True
    else:
      return False

  if j == 8: # Mill check for b3
    
    if( (board[Pieces.b5.value] == C and board[Pieces.b1.value] == C)):
      return True
    else:
      return False
    
  if j == 9: # Mill check for c3
    
    if( (board[Pieces.c2.value] == C and board[Pieces.c4.value] == C)):
      return True
    else:
      return False
  
  if j == 10: # Mill check for e3
    
    if( (board[Pieces.e2.value] == C and board[Pieces.e4.value] == C) or (board[Pieces.f3.value] == C and board[Pieces.g3.value] == C)):
      return True
    else:
      return False
    
  if j == 11: # Mill check for f3
    
    if( (board[Pieces.e3.value] == C and board[Pieces.g3.value] == C) or (board[Pieces.f1.value] == C and board[Pieces.f5.value] == C)):
      return True
    else:
      return False

  if j == 12: # Mill check for g3
    
    if( (board[Pieces.f3.value] == C and board[Pieces.e3.value] == C) or (board[Pieces.g0.value] == C and board[Pieces.g6.value] == C)):
      return True
    else:
      return False

  if j == 13: # Mill check for c4
    
    if( (board[Pieces.c2.value] == C and board[Pieces.c3.value] == C) or (board[Pieces.b5.value] == C and board[Pieces.a6.value] == C) or (board[Pieces.d4.value] == C and board[Pieces.e4.value] == C)):
      return True
    else:
      return False

  if j == 14: # Mill check for d4
    
    if( (board[Pieces.c4.value] == C and board[Pieces.e4.value] == C) or (board[Pieces.d5.value] == C and board[Pieces.d6.value] == C)):
      return True
    else:
      return False

  if j == 15: # Mill check for e4
    
    if( (board[Pieces.f5.value] == C and board[Pieces.g6.value] == C) or (board[Pieces.c4.value] == C and board[Pieces.d4.value] == C) or (board[Pieces.e3.value] == C and board[Pieces.e2.value] == C)):
      return True
    else:
      return False
  
  if j == 16: # Mill check for b5
    
    if( (board[Pieces.c4.value] == C and board[Pieces.a6.value] == C) or (board[Pieces.d5.value] == C and board[Pieces.f5.value] == C) or (board[Pieces.b1.value] == C and board[Pieces.b3.value] == C)):
      return True
    else:
      return False
     
  if j == 17: # Mill check for d5
    
    if( (board[Pieces.d4.value] == C and board[Pieces.d6.value] == C) or (board[Pieces.b5.value] == C and board[Pieces.f5.value] == C)):
      return True
    else:
      return False
  
  if j == 18: # Mill check for f5
    
    if( (board[Pieces.e4.value] == C and board[Pieces.g6.value] == C) or (board[Pieces.d5.value] == C and board[Pieces.b5.value] == C) or (board[Pieces.f1.value] == C and board[Pieces.f3.value] == C)):
      return True
    else:
      return False

  if j == 19: # Mill check for a6
    
    if( (board[Pieces.d6.value] == C and board[Pieces.g6.value] == C) or (board[Pieces.b5.value] == C and board[Pieces.c4.value] == C)):
      return True
    else:
      return False

  if j == 20: # Mill check for d6
    
    if( (board[Pieces.d5.value] == C and board[Pieces.d4.value] == C) or (board[Pieces.a6.value] == C and board[Pieces.g6.value] == C)):
      return True
    else:
      return False

  if j == 21: # Mill check for g6
    
    if( (board[Pieces.d6.value] == C and board[Pieces.a6.value] == C) or (board[Pieces.g3.value] == C and board[Pieces.g0.value] == C) or (board[Pieces.f5.value] == C and board[Pieces.e4.value] == C)):
      return True
    else:
      return False
# Generate Moves Opening Pseudo Code
def gen_move_open(board):
  L = []

  L = gen_add(board)
  
  return L  

def gen_move_mid_end(board):
  
  num_white = board.count('W')
  if num_white == 3:
    return gen_hop(board)

  return gen_move(board)

# Generate Add pseudo code
def gen_add(board):
  L = []
  for item in range(len(board)):
    if board[item] == 'x':
      b = board.copy()
      b[item] = 'W'
      if calc_mill(item, b):
        L = gen_remove(b, L)
      else:
        L.append(b)
  return L  

#Generate Hopping
def gen_hop(board):

  L=[]
  for i in range(len(board)):
    if board[i] == 'W':
      for j in range(len(board)):
        if board[j] == 'x':
          b = board.copy()
          b[i] = 'x'
          b[j] = 'W'
          if calc_mill(j,b):
            L = gen_remove(b,L)
          else:
            L.append(b)
  return L

#Gen Move
def gen_move(board):

  L=[]
  for i in range(len(board)):
    if board[i] == 'W':
      neigh = neighbors(i)

      for j in neigh :
        if board[j] == 'x':
          b = board.copy()
          b[i] = 'x'
          b[j] = 'W'
          if calc_mill(j, b):
            L = gen_remove(b, L)
          else:
            L.append(b)
  return L


# Generate Remove pseduo code
def gen_remove(board, L):
  n = len(L)
  for item in range(len(board)):
    if board[item] == 'B':
      if not calc_mill(item, board):
        b = board.copy()
        b[item] = 'x'
        L.append(b)
  if len(L) == n:
    L.append(board)
  return L


def static_opening(board):
  num_white = board.count('W')
  num_black = board.count('B')
  return num_white - num_black

def static_opening_black(board):
  num_black = board.count('W')
  num_white = board.count('B')
  return num_white - num_black

def static_mid_end(board):
  num_white = board.count('W')
  num_black = board.count('B')
  
  board = swap(board)
  L = gen_move_mid_end(board)

  black_moves = len(L)

  if num_black <= 2:
    return 10000
  elif num_white <= 2:
    return -10000
  elif black_moves == 0:
    return 10000
  
  return (1000 * (num_white - num_black) - black_moves)


def static_opening_improved(board):
  num_white = board.count('W')
  num_black = board.count('B')
  imp_white = 0
  imp_black = 0

  improved = [2,10,13,15,16,18,21]

  for pos in improved:
    if board[pos] == 'W':
      imp_white += 1
    elif board[pos] == 'B':
      imp_black += 1


  return num_white + (imp_white * 9) - num_black - (imp_black * 9)




def static_mid_end_imp(board):
  num_white = board.count('W')
  num_black = board.count('B')

  board = swap(board)
  L = gen_move_mid_end(board)
  black_moves = len(L)


  if num_black <= 2:
    return 10000
  elif num_white <= 2:
    return -10000
  elif black_moves == 0:
    return 10000
  else:
    nextmills = getnextmills(board)
    return (1000 * (num_white - num_black) + 1000 * nextmills - black_moves)

def getnextmills(board):

  result = 0

  for item in range(len(board)):
    if board[item] == 'x':
      b = board.copy()
      b[item] = 'W'
      if calc_mill(item,b):
        result += 1
  
  return result

