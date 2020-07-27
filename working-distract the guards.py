import math

def isALoop(x, y):
    if y > x:
        return isALoop(y, x)
    z = (x + y) / math.gcd(x, y)
    return not isPowerOfTwo(z)

def isPowerOfTwo(n):
    return math.log2(n).is_integer()

def solution(arr):
    def pair(u, match, seen):
        for v in range(l):
            if M[u][v] and seen[v] == False:
                seen[v] = True
                
                # if a has been matched to b, retrieve a from match[b]
                # check if it can be matched to another number given the 
                # current seen list. If so, updated match[b] to c (current)
                if match[v] == -1 or pair(match[v], match, seen):
                    match[v] = u
                    return True
        return False

           
    # build graph
    l = len(arr)
    M = [[None] * l for _ in range(l)]
    
    for i in range(l):
        for j in range(i, l):
            M[i][j] = isALoop(arr[i], arr[j])
            M[j][i] = M[i][j]  
    
    match = [-1] * l
    result = 0
    for i in range(l):
        seen = [False] * l
        if pair(i, match, seen):
            result += 1
    return l - 2 * (result//2) 