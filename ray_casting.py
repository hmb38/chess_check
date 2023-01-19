#wrtite function which returns a list of in line of sight positions given a starting position and a direction
def pos_in_bounds(pos):
  x,y = pos
  if 0 < x and x < 9 and 0 < y and y < 9: 
    return True
  else:
    return 
    
def add_direction_to_pos(pos, direction):
  return (pos[0] + direction[0], pos[1] + direction[1])
  
def find_los_posns(start_pos, direction):
  los_posns = []
  pos = tuple(start_pos)
  while pos_in_bounds(add_direction_to_pos(pos,direction)):
    pos = add_direction_to_pos(pos,direction)
    los_posns.append(pos)
  return los_posns

# def find_blocking_positions(king,piece, pieces):
#   ........
  
def test_find_los_posns():
  print(find_los_posns((0,0),(0,-1)))
  print(find_los_posns((6,3),(1,1)))
  print(find_los_posns((8,8),(1,1)))
  print(find_los_posns((8,8),(-1,-1)))
def test_pos_in_bounds():
  print(pos_in_bounds((-1,3)), False) #should be False
  print(pos_in_bounds((4,5)),True) #should be True
  print(pos_in_bounds((8,9)), False) #should be False
  print(pos_in_bounds((1,1)), True) #should be True
  print(pos_in_bounds((1,0)), False) #should be False
  print(10,"hello")
test_find_los_posns()
#test_pos_in_bounds()

# 

