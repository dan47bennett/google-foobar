class cell: 
  def __init__(self, x = 0, y = 0, distance = 0):
    self.x = x 
    self.y = y 
    self.distance = distance 


def convertToXY(boardPosition):
    y = boardPosition // 8
    x = boardPosition - 8 * y
    return x, y


def isInsideBoard(x, y):
  if 0 <= x <= 7 and 0 <= y <= 7:
    return True
  return False


def solution(src, dest): 
  deltaX = [2, 2, -2, -2, 1, 1, -1, -1] 
  deltaY = [1, -1, 1, -1, 2, -2, 2, -2] 

  visitedSquaresData = []

  (xStart, yStart) = convertToXY(src)
  (xFinal, yFinal) = convertToXY(dest)

  visitedSquaresData.append(cell(xStart, yStart, 0))

  visitedSquaresBoolean = [[False for i in range(8)] for j in range(8)] 
    
  visitedSquaresBoolean[xStart][yStart] = True

  while(len(visitedSquaresData) > 0): 
          
    currentCell = visitedSquaresData[0] 
    visitedSquaresData.pop(0) 
    if(currentCell.x == xFinal and currentCell.y == yFinal): 
        return currentCell.distance 
          
    for i in range(8):    
      x = currentCell.x + deltaX[i] 
      y = currentCell.y + deltaY[i]
        
      if(isInsideBoard(x, y) and not visitedSquaresBoolean[x][y]): 
        visitedSquaresBoolean[x][y] = True
        visitedSquaresData.append(cell(x, y, currentCell.distance + 1))


answer = solution(0,1)
print(answer)