def solution(n):
    intN = int(n)
    return quickestPath(intN)

    
def quickestPath(n):
    count = 0
    while n > 1:

        if n % 2 == 0:
            n = n / 2

        elif n == 3 or n % 4 == 1:
            n -= 1

        else:
            n += 1

        count += 1
    return count