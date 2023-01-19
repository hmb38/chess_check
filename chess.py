from pprint import pprint

# def any_king_is_in_check (pieces):
# 	all_kings = find_kings(pieces)
# 	for k in all_kings:
# 		if king_is_in_check(pieces, k):
# 			return True
# 	return False

def king_is_in_check(pieces, king):
	for piece in pieces:
		if threatens_king(king, piece, pieces):
			return True
	return False

def pawn_threatens_king(king, piece, pieces):
  if king["colour"] == "White":
    attacking_direction = 1
  else: 
    attacking_direction = -1
  return (abs(piece["pos"]["x"] - king["pos"]["x"]) == 1 and 
         piece["pos"]["y"] == king["pos"]["y"] + attacking_direction)
  
def bishop_threatens_king(king, piece, pieces):
  king_x = king["pos"]["x"]
  king_y = king["pos"]["y"]
  piece_x = piece["pos"]["x"]
  piece_y = piece["pos"]["y"]
  if (king_x - king_y) == (piece_x - piece_y) or (king_x + king_y) == (piece_x + piece_y)
    return True
  return False

def knight_threatens_king(king, piece, pieces):
  king_x = king["pos"]["x"]
  king_y = king["pos"]["y"]
  piece_x = piece["pos"]["x"]
  piece_y = piece["pos"]["y"]
  return (king_x - piece_x)**2 + (king_y - piece_y)**2 == 5

  
def threatens_king(king, piece, pieces):
  if piece["colour"] == king["colour"]:
    return False
  if piece["type"] == "Pawn":
    return pawn_threatens_king(king, piece, pieces)
  if piece["type"] == "Knight":
    return knight_threatens_king(king, piece, pieces)
  if piece["type"] == "Bishop":
    return bishop_threatens_king(king, piece, pieces)
  return False
   
def any_threatens_king(king, pieces):
  for p in pieces:
    if threatens_king(king, p, pieces):
      return p
  return False

# Need to break the above into single letters
def parse_concise_board (concise_board):
  Cells = [list(concise_board[x]) for x in range(len(concise_board))]
  List_Pieces = []
  for i in range(len(Cells)):
    for j in range(len(Cells[i])):
      Cell = Cells[i][j]
      if Cell != ".":
        Piece = {
          "type": Get_Piece_Type(Cell),
          "colour": Get_Piece_Colour(Cell),
          "pos": {
            "x": j + 1,
            "y": i + 1
          }
        }
        List_Pieces.append(Piece)
  return List_Pieces




#def Change_Piece_Info (x)
def Get_Piece_Type(Cell_Val):
  Ref_Names = {
    "b": "Bishop",
    "p": "Pawn",
    "r": "Rook",
    "h": "Knight",
    "k": "King",
    "q": "Queen",
    ".": ""
  }
  Type = Ref_Names[Cell_Val.lower()]
  return Type

def Is_Upper(Cell_Val):
  if Cell_Val.upper() == Cell_Val:
    return True
  else:
    return False
    
def Get_Piece_Colour(Cell_Val):
  if Is_Upper(Cell_Val):
    return "Black"
  else:
    return "White"


def is_white_king(piece):
  return piece["type"] == "King" and piece["colour"] == "White"

def is_black_king(piece):
  return piece["type"] == "King" and piece["colour"] == "Black"

def is_black_pawn(piece):
  return piece["type"] == "Pawn" and piece["colour"] == "Black"

starting_board_concise = ("rhbqkbhr", "pppppppp", "........", "........", "........", "........", "PPPPPPPP", "RHBKQBHR")