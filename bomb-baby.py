def solution(x, y):
    intX = int(x)
    intY = int(y)
    return numberOfGenerations(intX, intY)


def numberOfGenerations(x, y):
    generations = 0
    while x != 1 or y != 1:
        
        if x == y or x < 1 or y < 1:
            return 'impossible'

        if x > 2 * y:
            estimatedGenerations = int(x / y)
            generations += estimatedGenerations - 1
            x = x - ((estimatedGenerations - 1) * y)
        
        elif y > 2 * x:
            estimatedGenerations = int(y / x)
            generations += estimatedGenerations - 1
            y = y - ((estimatedGenerations - 1) * x)
    
        elif x > y:
            generations += 1
            x = x - y

        else:
            generations += 1
            y = y - x

    return str(generations)
