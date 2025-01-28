import math

def isPrime(k):
    if k < 2:
        return False
    
    for i in range(2, int(math.sqrt(k))):
        if k % i == 0:
            return False
        
    return True