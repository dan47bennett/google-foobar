import math



# a pair will create a loop if x + y / gcd is not a power of two
def isALoop(x, y):
    if y > x:
        return isALoop(y, x)
    z = (x + y) / math.gcd(x, y)
    return not isPowerOfTwo(z)
       

def isPowerOfTwo(n):
    return math.log2(n).is_integer()
  

def bananaGraph(bananaList):
    graph = {i: [] for i in range(len(bananaList))}
    for i, a in enumerate(bananaList):
        for j, b in enumerate(bananaList):
            if i != j and isALoop(a, b):
                graph[i].append(j)
    return graph

def solution(banana_list):
    graph = bananaGraph(banana_list)
    m = Matching.from_graph(graph)
    matches = find_maximum_matching(graph, m)
    return len(banana_list) - len(matches)


print(solution([1, 7, 3, 21, 13, 19]))