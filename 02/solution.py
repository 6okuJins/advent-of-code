class Solution():
  winningMoves = {('A', 'Y'), ('B', 'Z'), ('C', 'X')}
  tieMoves = {('A', 'X'), ('B', 'Y'), ('C', 'Z')}
  losingMoves = {('A', 'Z'), ('B', 'X'), ('C', 'Y')}
  pointValues = { 'X': 1,
                  'Y': 2,
                  'Z': 3}

  def __init__(self, inputList):
    self.inputList = inputList
    self.score = 0

  def getInputList(self):
    return self.inputList
  
  def setScore(self, points):
    self.score += points
  
  def getScore(self):
    return self.score

  def computeScore(self):
    inputList = self.getInputList()
    for pair in inputList:
      self.setScore(self.pointValues[pair[1]])
      if pair in self.winningMoves:
        self.setScore(6)
      elif pair in self.tieMoves:
        self.setScore(3)
  
  def computeScore2(self):
    inputList = self.getInputList()
    for pair in inputList:
      # If you are meant to lose
      if pair[1] == 'X':
        self.setScore(self.pointValues[dict(self.losingMoves)[pair[0]]])
      # If you are meant to tie
      elif pair[1] == 'Y':
        self.setScore(self.pointValues[dict(self.tieMoves)[pair[0]]] + 3)
      else:
        self.setScore(self.pointValues[dict(self.winningMoves)[pair[0]]] + 6)

if __name__ == "__main__":
  inputList = []
  with open('input.txt') as f:
    for pair in f:
      inputList.append(tuple(pair.rstrip('\n').split(" ")))
  mySolution = Solution(inputList)
  mySolution.computeScore2()
  print(mySolution.getScore())
  