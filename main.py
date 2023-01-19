from pprint import pprint
from chess import parse_concise_board , any_threatens_king , is_black_king, is_white_king

def test_random_stuff():
  # k is white king
  example_board_concise1 = (
    ".....P..", 
    "..ppp...", 
    "..pkp.PB", 
    "P....h..",
    "BB.B....", 
    "........", 
    ".....p..", 
    "....K..."
  )
  
  pieces = parse_concise_board(example_board_concise1)
 
  black_king = list(filter(is_black_king, pieces))[0]
  
  white_king = list(filter(is_white_king, pieces))[0]
   
  result_1 = any_threatens_king(white_king, pieces)
  if result_1:
    print(result_1 , "There is a king in check")
  else:
    print("White king not in check")
test_random_stuff()