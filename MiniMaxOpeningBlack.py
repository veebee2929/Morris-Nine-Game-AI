#MiniMaxOpeningBlack V2
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

def minmaxopen(pos, next, depth):
  global static_pos

  temp_board = pos.copy()

  if depth == 0:
    static_pos += 1
    return static_opening(temp_board)

  if next :
    max_est = float('inf')

    temp_board = swap(temp_board)
    prob_open = gen_move_open(temp_board)

    for item in prob_open:
      item = swap(item)

    for item in prob_open:
      curr = minmaxopen(pos = item,  next = False, depth = depth - 1)
      max_est = min(max_est, curr)
  
  else:
    max_est = float('-inf')

    prob_open = gen_move_open(temp_board)

    for item in prob_open:
      curr = minmaxopen(pos = item,  next = True, depth = depth - 1)
      max_est = max(max_est, curr)

  return max_est


opening = ''
max_est = float("-inf")
static_pos = 0
board1 = list(open(input, 'r').read())

board1 = swap(board1)

L = gen_move_open(board1)


for i in L :
  #True is min and False is Max
  curr = minmaxopen(pos = i, next= True, depth = depth - 1)

  if curr > max_est:
    max_est = curr
    opening = i

opening = swap(opening)

output = open(output,"w")
output.write("Board Position: {}.".format(''.join(opening)))
output.write("\nPositions evaluated by Static estimation: {}.".format(static_pos))
output.write("\nMINIMAX estimate: {}.".format(-max_est))
