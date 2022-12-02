with open('input.txt') as f:
  sumsArray = []
  currentSum = 0
  for line in f:
    currentNum = line.rstrip()
    if currentNum:
      currentSum += int(currentNum)
    else:
      sumsArray.append(currentSum)
      currentSum = 0
  sumsArray.append(currentSum)
  sumsArray.sort()
  print(max(sumsArray))
  print(sumsArray.pop() + sumsArray.pop() + sumsArray.pop())
