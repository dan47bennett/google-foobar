def findParent(height, node): 
    start = 1
    end = (2 ** height) - 1
    if (end == node): 
        return -1
    while(node >= 1): 
        end = end - 1
        midPoint = start + (end - start) // 2
        if(midPoint == node or end == node): 
            return (end + 1) 
        elif (node < midPoint): 
            end = midPoint 
        else: 
            start = midPoint



def solution(h, q):
    arrayOfParents = []
    for value in q:
        parentNode = findParent(h, value)
        arrayOfParents.append(parentNode)
    return arrayOfParents


answer = solution(3, [7, 3, 5, 1])
print(answer)