import itertools

example = [
  [0, 2, 2, 2, -1],  # 0 = Start
  [9, 0, 2, 2, -1],  # 1 = Bunny 0
  [9, 3, 0, 2, -1],  # 2 = Bunny 1
  [9, 3, 2, 0, -1],  # 3 = Bunny 2
  [9, 3, 2, 2,  0],  # 4 = Bulkhead
]

def toPath(permutation):
  permutation = list(permutation)
  permutation = [0] + permutation + [-1]
  path = list()
  for i in range(1, len(permutation)):
    path.append((permutation[i - 1], permutation[i]))
  return path


def floydsAlgorithm(times):
  N = len(times)
  for k in range(N):
    for i in range(N):
      for j in range(N):
        replacement = times[i][k] + times[k][j]
        if times[i][j] > replacement:
          times[i][j] = replacement
  return times


def solution(time, timeLimit):
  numberOfBunnies = len(time) - 2

  time = floydsAlgorithm(time)

  for i in range(len(time)):
    if time[i][i] < 0:
      return [j for j in range(numberOfBunnies)]
  
  for i in reversed(range(numberOfBunnies + 1)):
    for permutation in itertools.permutations(range(1, numberOfBunnies + 1), i):
      totalTime = 0
      path = toPath(permutation)
      for start, end in path:
        totalTime += time[start][end]
      if totalTime <= timeLimit:
        return sorted(list(i - 1 for i in permutation))

answer = solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1)
print(answer)

