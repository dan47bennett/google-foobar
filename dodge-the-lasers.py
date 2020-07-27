# express sqrt(2) as a long integer divided by a large factor of 10

sqrt2Long = int("41421356237309504880168872420969807856967187537694807317667973799073247846210703885038753432764157273501384623091229702492483605585073721264412149709993583141322266592750559275579995050115278206")
factorOfTen = int("100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")


def sumUpTo(n):
  return int(n * (n + 1) // 2)

def beattySum(n):
  if n < 1:
    return 0
  if n == 1:
    return 1

  # initialise total
  total = int(n * (n + 1) // 2)
  
  nPrime = int(n * sqrt2Long // factorOfTen)
  total += (n * nPrime) - sumUpTo(nPrime) - beattySum(nPrime)
  return total

def solution(nStr):
  n = int(nStr)
  return str(int(beattySum(n)))

ans = solution(str(10000000000000))
print(ans)
