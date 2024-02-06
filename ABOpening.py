#ABOpening
import sys

from pseudo import *

input = sys.argv[1]
output = sys.argv[2]
depth = int(sys.argv[3])

def swap(board):

  for i in range(len(board)):
    if board[i] == 'W':
      board[i] = 'B'
    elif board[i] == 'B':
      board[i] = 'W'
  return board


def abopen(pos, alpha, beta, depth, next):
  global static_pos

  temp_board = pos.copy()
  
  if depth == 0:
    static_pos += 1
    return static_opening(temp_board)

  if next:
    max_est = float('inf')

    temp_board = swap(temp_board)
    
    prob_open = gen_move_open(temp_board)

    for item in prob_open:
      item = swap(item)
    
    for item in prob_open:
      curr = abopen(item, alpha, beta, depth - 1, next = False)
      max_est = min(max_est, curr)
      
      if max_est <= alpha:
        return max_est
      else:
        beta = min(beta, max_est)
      
  else :
    max_est = float('-inf')

    prob_open = gen_move_open(temp_board)
    
    for item in prob_open:
      curr = abopen(item, alpha, beta, depth - 1, next = True)
      max_est = max(curr, max_est)
      
      if max_est >= beta:
        return max_est
      else:
        alpha = max(max_est, alpha)

  return max_est

opening = ''
max_est = float("-inf")
static_pos = 0
board1 = list(open(input, 'r').read())

L = gen_move_open(board1)
alpha = float('-inf')
beta = float('inf')

for i in L:
  curr = abopen(i, alpha, beta, depth - 1, next = True )

  if curr > max_est:
    max_est = curr
    opening = i
    if max_est >= beta:
      break
    else :
      alpha = max(max_est, alpha)
      
      
output = open(output,"w")
output.write("Board Position: {}.".format(''.join(opening)))
output.write("\nPositions evaluated by Static estimation: {}.".format(static_pos))
output.write("\nMINIMAX estimate: {}.".format(max_est))      
