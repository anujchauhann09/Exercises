import time
from ..math_utils import isPrime

def count_primes_sequential(limit):
    start_time = time.time()
    prime_count = 0
    
    for num in range(2, limit + 1):
        if isPrime(num):
            prime_count += 1

    end_time = time.time()
    return prime_count, end_time - start_time